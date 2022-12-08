# -*- coding: utf-8 -*-

"""
access_db_controller.py: The python file dedicated to the "Controller" part of the MVC pattern implemented within
the "PRESENTATION" layer of the Project.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"


from CONFIGURATIONS.logger import LOGGER
from CONFIGURATIONS.application_properties import get_application_property

from PRESENTATION.VIEW.access_db_view import AccessDBView

from BUSINESS.MODEL.DOMAIN_OBJECT.line_to_write_do import LineToWriteDO
from BUSINESS.MODEL.DOMAIN_OBJECT.stanica_do import StanicaDO

from BUSINESS.SERVICE.APPLICATION_SERVICE.INTF.access_db_as_intf import AccessDBASIntf
from BUSINESS.SERVICE.APPLICATION_SERVICE.IMPL.access_db_as_impl import AccessDBASImpl


class AccessDBController:

    def set_access_db_view(self, access_db_view: AccessDBView):
        self.access_db_view = access_db_view

    def get_access_db_view(self) -> AccessDBView:
        return self.access_db_view

    def set_access_db_as(self, access_db_as: AccessDBASIntf):
        self.access_db_as = access_db_as

    def get_access_db_as(self) -> AccessDBASIntf:
        return self.access_db_as

    def set_current_list_of_stanica(self, current_list_of_stanica: list):
        self.current_list_of_stanica = current_list_of_stanica

    def get_current_list_of_stanica(self) -> list:
        return self.current_list_of_stanica

    def __init__(self, *args):
        if len(args) == 1:
            # The View part was provided
            self.set_access_db_view(args[0])

            # Initializing the AS to be used by the current Controller
            self.set_access_db_as(AccessDBASImpl())

            # We have to feed the label for the fixed strings
            parameter_1_string = get_application_property("parameter1")
            parameter_2_string = get_application_property("parameter2")
            self.get_access_db_view().get_window_ui().get_label_post_process().setText(
                parameter_1_string + " - " + parameter_2_string
            )

            # Now, let's assign the specific action of saving all of the information to the "Potvrid" button
            self.get_access_db_view().get_window_ui().get_button_potvrdi().clicked.connect(self.save_information)

            # Let's load the first line
            self.load_lines()

            # First, let's have clear boxes
            self.get_access_db_view().get_window_ui().get_combo_box_team().setCurrentIndex(-1)
            self.get_access_db_view().clear_all_boxes()

            # Management of the events related to all the elements on the GUI
            self.manage_events()

    def load_lines(self):
        """
        Loading the values of the filtered lines at the level of the View part
        :return:
        """
        try:
            # First, let's retrieve the filtered data (lines)  from the Excel File
            lines = self.get_access_db_as().get_lines(
                get_application_property("excel_file_path")
            )
            self.set_current_list_of_stanica(self.filter_stanica(lines))

            # A counter that we will use when it will come to managing "Stanica"'s items feedings
            stanica_item_counter = 0
            # Let's feed the "Stanica"'s combo box
            for line in sorted(self.get_current_list_of_stanica(), key=lambda x: str(x.get_label), reverse=False):
                self.get_access_db_view().get_window_ui().get_combo_box_stanica().addItem(line.get_label())
                # Managing the event specific to the current item
                self.get_access_db_view().get_window_ui().get_combo_box_stanica().currentIndexChanged.connect(
                    self.feed_combo_box_predmet
                )
                stanica_item_counter += 1
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Loading Process. "
            )
            raise

    def manage_events(self):
        """
        Activating each element in function of the Workflow provided
        :return:
        """
        view = self.get_access_db_view()
        view_window = view.get_window_ui()

        view_window.get_combo_box_team().currentIndexChanged.connect(self.activate_combo_box_stanica)

        view_window.get_combo_box_predmet().currentIndexChanged.connect(self.activate_combo_box_kod_greske)

        view_window.get_combo_box_kod_greske().currentIndexChanged.connect(self.activate_buttons_n)

        for button in view.get_list_of_left_buttons():
            button.clicked.connect(self.activate_button_potvrdi)

    def activate_combo_box_stanica(self):
        """
        Activating the Combo Box Stanica.
        :return:
        """
        view = self.get_access_db_view()
        view_window = view.get_window_ui()
        if view_window.get_combo_box_team().currentIndex() != -1:
            view_window.get_combo_box_stanica().setEnabled(True)

    def activate_combo_box_kod_greske(self):
        """
         Activating the Combo Box Kod Greske.
        :return:
        """
        view = self.get_access_db_view()
        view_window = view.get_window_ui()
        if view_window.get_combo_box_predmet().currentIndex() != -1:
            view_window.get_combo_box_kod_greske().setEnabled(True)

    def activate_buttons_n(self):
        """
        Activating the label N and all its related Buttons (Minus & Plus)
        :return:
        """
        view = self.get_access_db_view()
        view_window = view.get_window_ui()
        if view_window.get_combo_box_kod_greske().currentIndex() != -1:
            view_window.get_button_plus().setEnabled(True)
            view_window.get_button_minus().setEnabled(True)
            # Since O is accepted for N, let's directly activate all the left buttons
            for button in view.get_list_of_left_buttons():
                button.setEnabled(True)

    def activate_button_potvrdi(self):
        if self.get_access_db_view().get_current_left_button_selected() is not None:
            self.get_access_db_view().get_window_ui().get_button_potvrdi().setEnabled(True)
            self.get_access_db_view().get_window_ui().get_button_potvrdi().setStyleSheet(
                u"background-color: #1c2632;\n"
                "color: #f7471f;\n"
                "border : 5px solid ;\n"
                "border-radius: 25px;\n"
                "border-color: #f7471f;"
            )

    def filter_stanica(self, raw_lines: list) -> list:
        """

        :param raw_lines: The Raw lines to be filtered
        :return: A list of lines in which they are grouped by their Stanica's Label
        """
        list_to_return = []
        stanica_marks = []
        for line in raw_lines:
            if line.get_cells() not in stanica_marks:
                stanica_marks.append(line.get_cells())
                new_stanica = StanicaDO(line.get_cells())
                if not (str(line.get_material_dpn()) == "nan"):
                    line_material_dpn = line.get_material_dpn()
                else:
                    line_material_dpn = ""
                if not (str(line.get_material_l_code()) == "nan"):
                    line_material_l_code = line.get_material_l_code()
                else:
                    line_material_l_code = ""
                new_stanica.get_predmets().append(line_material_dpn)
                new_stanica.get_predmets().append(line_material_l_code)
                list_to_return.append(new_stanica)
            else:
                existing_stanica = [x for x in list_to_return if x.get_label() == line.get_cells()][0]
                if not (str(line.get_material_dpn()) == "nan"):
                    line_material_dpn = line.get_material_dpn()
                else:
                    line_material_dpn = ""
                if not (str(line.get_material_l_code()) == "nan"):
                    line_material_l_code = line.get_material_l_code()
                else:
                    line_material_l_code = ""
                existing_stanica.get_predmets().append(line_material_dpn)
                existing_stanica.get_predmets().append(line_material_l_code)
        return list_to_return

    def save_information(self):
        """
        Saving all the information within the GUI to the DB, and then clearing the GUI

        :return:
        """
        try:
            # First, let's get all the information...
            view = self.get_access_db_view()
            view_window = view.get_window_ui()
            area = view_window.get_label_post_process().text()
            station = view_window.get_combo_box_stanica().currentText()
            item = view_window.get_combo_box_predmet().currentText()
            defect = view_window.get_combo_box_kod_greske().currentText()
            quantity = view_window.get_label_n().text()
            material = view.get_current_left_button_selected().text()
            team = view_window.get_combo_box_team().currentText()
            zone = get_application_property("zone")

            # ...then, we store them within a LineToWrite DO
            line_to_save = LineToWriteDO()
            line_to_save.set_area(area)
            line_to_save.set_station(station)
            line_to_save.set_item(item)
            line_to_save.set_defect(defect)
            line_to_save.set_defect(defect)
            line_to_save.set_quantity(int(quantity))
            line_to_save.set_material(material)
            line_to_save.set_team(int(team))
            line_to_save.set_zone(zone)

            # Then, let's save them
            time_of_writing = self.get_access_db_as().write_line(line_to_save)

            # Finally, let's clear the GUI in function of the Current Time
            if time_of_writing.time().minute == 0:
                if time_of_writing.time().hour == 6 \
                        or time_of_writing.time().hour == 14 \
                        or time_of_writing.time().hour == 22:
                    # Clearing the GUI's content
                    self.get_access_db_view().clear_all_boxes()
                else:
                    self.get_access_db_view().clear_all_boxes()
                    self.get_access_db_view().get_window_ui().get_combo_box_team().setCurrentIndex(-1)
            else:
                self.get_access_db_view().clear_all_boxes()
                self.get_access_db_view().get_window_ui().get_combo_box_team().setCurrentIndex(-1)
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the SavingProcess. "
            )
            raise

    def feed_combo_box_predmet(self, index):
        """
        Feeding the Combo Box dedicated to the "Predmet" from the value of that of "Stanica"

        :param index: The index of the Stanica's item currently selected
        :return: None
        """
        if index > -1:
            try:
                self.get_access_db_view().get_window_ui().get_combo_box_predmet().setEnabled(True)
                combo_box_stanica = self.get_access_db_view().get_window_ui().get_combo_box_stanica()
                current_stanica_label = combo_box_stanica.currentText()
                current_stanica = [x for x in self.get_current_list_of_stanica()
                                   if x.get_label() == current_stanica_label][0]

                self.get_access_db_view().get_window_ui().get_combo_box_predmet().clear()
                for predmet in sorted(current_stanica.get_predmets(), key=str, reverse=False):
                    if predmet:
                        self.get_access_db_view().get_window_ui().get_combo_box_predmet().addItem(str(predmet))
                self.get_access_db_view().get_window_ui().get_combo_box_predmet().setCurrentIndex(-1)
                self.get_access_db_view().get_window_ui().get_combo_box_kod_greske().setEnabled(False)
            except Exception as exception:
                # At least one error has occurred, therefore, stop the process
                LOGGER.error(
                    exception.__class__.__name__ + ": " + str(exception)
                    + ". Can't go further with the Feeding Process. "
                )
                raise
