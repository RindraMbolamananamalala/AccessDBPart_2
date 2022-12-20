# -*- coding: utf-8 -*-

"""
accessdb_pii_controller.py: The python file dedicated to the "Controller" part of the MVC pattern implemented within
the "PRESENTATION" layer of the Project.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from functools import partial

import decimal
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from CONFIGURATIONS.logger import LOGGER


from PRESENTATION.VIEW.accessdb_pii_main_window_view import AccessDBPIIMainWindowView

from PRESENTATION.VIEW.WIDGET.accessdb_pii_content_view import AccessDBPIIContentView
from PRESENTATION.VIEW.WIDGET.accessdb_pii_content_zone_view import AccessDBPIIContentZoneView
from PRESENTATION.VIEW.WIDGET.accessdb_pii_content_familije_view import AccessDBPIIContentFamilijeView
from PRESENTATION.VIEW.WIDGET.accessdb_pii_content_body_zone_view import AccessDBPIIContentBodyZoneView
from PRESENTATION.VIEW.WIDGET.accessdb_pii_content_body_area_view import AccessDBPIIContentBodyAreaView

from PRESENTATION.VIEW.FORM.form_weight_material_view import FormWeightMaterialView
from PRESENTATION.VIEW.FORM.form_weights_validation_view import FormWeightsValidationView


from BUSINESS.MODEL.DOMAIN_OBJECT.line_excel_submition_do import LineExcelSubmitionDO
from BUSINESS.MODEL.DOMAIN_OBJECT.line_weights_do import LineWeightsDO

from BUSINESS.SERVICE.APPLICATION_SERVICE.INTF.accessdb_pii_as_intf import AccessDBPIIASIntf
from BUSINESS.SERVICE.APPLICATION_SERVICE.IMPL.accessdb_pii_as_impl import AccessDBPIIASImpl
from BUSINESS.SERVICE.APPLICATION_SERVICE.INTF.excel_as_intf import ExcelASIntf
from BUSINESS.SERVICE.APPLICATION_SERVICE.IMPL.excel_as_impl import ExcelASImpl


class AccessDBPIIController:

    def set_accessdb_pii_main_window_view(self, accessdb_pii_main_window_view: AccessDBPIIMainWindowView):
        """

        :param accessdb_pii_main_window_view: The main window VIEW of the Application
        :return: None
        """
        self.accessdb_pii_main_window_view = accessdb_pii_main_window_view

    def get_accessdb_pii_main_window_view(self) -> AccessDBPIIMainWindowView:
        """

        :return: The main window VIEW of the Application
        """
        return self.accessdb_pii_main_window_view

    def set_accessdb_pii_as(self, accessdb_pii_as: AccessDBPIIASIntf):
        """

        :param accessdb_pii_as: The Access DB Part II general Application Service object to be used by the Controller
        :return: None
        """
        self.accessdb_pii_as = accessdb_pii_as

    def get_accessdb_pii_as(self) -> AccessDBPIIASIntf:
        """

        :return: The Access DB Part II general Application Service object used by the Controller
        """
        return self.accessdb_pii_as

    def set_excel_as(self, excel_as: ExcelASIntf):
        """

        :param excel_as: The Excel Application Service object to be used by the Controller.
        :return:
        """
        self.excel_as = excel_as

    def get_excel_as(self) -> ExcelASIntf:
        """

        :return: The Excel Application Service object used by the Controller.
        """
        return self.excel_as

    def set_current_main_window_content_view(self, current_main_window_content_view: AccessDBPIIContentView):
        """

        :param current_main_window_content_view:  The current content VIEW of the Main Window
        :return: None
        """
        self.current_main_window_content_view = current_main_window_content_view

    def get_current_main_window_content_view(self) -> AccessDBPIIContentView:
        """

        :return: The current content VIEW of the Main Window
        """
        return self.current_main_window_content_view

    def set_forms_weights_materials_views(self, forms_weights_materials_views: list):
        """

        :param forms_weights_materials_views: The list of Form Views in charge of the Recording of Weights
        for the different Categories
        :return: None
        """
        self.forms_weights_materials_views = forms_weights_materials_views

    def get_forms_weights_materials_views(self) -> list:
        """

        :return: The list of Form Views in charge of the Recording of Weights for the different Categories
        """
        return self.forms_weights_materials_views

    def set_form_weights_validation_view(self, form_weights_validation_view: FormWeightsValidationView):
        """

        :param form_weights_validation_view: The VIEW corresponding to the Form in charge of the validation of the
        weights inserted by the User
        :return:
        """
        self.form_weights_validation_view = form_weights_validation_view

    def get_form_weights_validation_view(self) -> FormWeightsValidationView:
        """

        :return: The VIEW corresponding to the Form in charge of the validation of the weights inserted by the User
        """
        return self.form_weights_validation_view

    def set_current_area_selected(self, current_area_selected: str):
        """

        :param current_area_selected: The current "Area" parameter selected
        :return:
        """
        self.current_area_selected = current_area_selected

    def get_current_area_selected(self) -> str:
        """

        :return: The current "Area" parameter selected
        """
        return self.current_area_selected


    def set_current_weight_category(self, current_weight_category: str):
        """

        :param current_weight_category: The Current Category of weight whose corresponding Form is opened for recording
        :return:
        """
        self.current_weight_category = current_weight_category

    def get_current_weight_category(self):
        """

        :return: The Current Category of weight whose corresponding Form is opened for recording
        """
        return self.current_weight_category

    def set_current_recorded_weights(self, current_recorded_weighs: list):
        """

        :param current_recorded_weighs: The list corresponding to the Weights currently recorded thanks to the Forms
        :return: None
        """
        self.current_recorded_weighs = current_recorded_weighs

    def get_current_recorded_weighs(self):
        """

        :return: The list corresponding to the Weights currently recorded thanks to the Forms
        """
        return self.current_recorded_weighs

    def __init__(self):
        # Initializing the AccessDB Part II's Main Window's VIEW
        self.set_accessdb_pii_main_window_view(AccessDBPIIMainWindowView())

        # Initializing all the ASs to be used by the Controller
        self.set_accessdb_pii_as(AccessDBPIIASImpl())
        self.set_excel_as(ExcelASImpl())

        # Initializing all the VIEWs of the Forms related to the Weighs specification of all the Categories
        self.set_forms_weights_materials_views([])
        """
        List of Category
        # Category 1 : Aluminium
        # Category 2 : Copper
        # Category 3 : Plastic
        # Category 4 : Terminal
        # Category 5 : Harness
        """
        self.categories_labels = ["Aluminijum", "Bakar", "Plastika", "Terminal", "Harness"]
        for category in self.categories_labels:
            self.get_forms_weights_materials_views().append(FormWeightMaterialView(category))

        # Initializing the VIEW corresponding to the Form for the validation of Weights
        self.set_form_weights_validation_view(FormWeightsValidationView())

        # Initializing the current "Area" selected  to None, its final confirmation will be done once the
        # Business Logic has been launched
        self.set_current_area_selected(None)

        # Initializing the list corresponding to the Weights currently recorded with an Empty list
        self.set_current_recorded_weights([])

        main_window_view = self.get_accessdb_pii_main_window_view()

        # The "Content Zone" will be the first Widget Content to be displayed at the beginning
        content_zone_view = AccessDBPIIContentZoneView(main_window_view.get_corresponding_hmi().get_widget_content())
        self.get_accessdb_pii_main_window_view().set_content_view(
            content_zone_view
        )
        self.set_current_main_window_content_view(content_zone_view)

        # Managing the whole set of Events
        self.manage_events()

    def manage_events(self):
        """
        Managing all the set of Events related to the Application
        :return: None
        """

        # When one of the Buttons within the "Content Zone" is clicked, the user may have in visual the "Content
        # Familije", or, the READ process on the first DB will directly happen, in function of the Zone's option chosen
        if isinstance(self.get_current_main_window_content_view(), AccessDBPIIContentZoneView):
            content_zone_options = self.get_current_main_window_content_view().get_corresponding_hmi() \
                .get_content_zone_options()
            for button in content_zone_options:
                button.clicked.connect(partial(self.pass_content_zone, button))

        # When one of the Buttons within the "Content Familije" is clicked, the user may have in visual the "Body zone",
        # or, the READ process on the first DB will directly happen, in function of the Familije's option chosen
        if isinstance(self.get_current_main_window_content_view(), AccessDBPIIContentFamilijeView):
            content_familije_options = self.get_current_main_window_content_view().get_corresponding_hmi() \
                .get_content_familije_options()
            for button in content_familije_options:
                button.clicked.connect(partial(self.pass_content_familije, button))

        # When one of the Buttons within the "Content Body Zone" is clicked, the user may have in visual the
        # "Body area", or, the READ process on the first DB will directly happen, in function of the
        # Body Zone's option chosen
        if isinstance(self.get_current_main_window_content_view(), AccessDBPIIContentBodyZoneView):
            content_body_zone_options = self.get_current_main_window_content_view().get_corresponding_hmi() \
                .get_content_body_zone_options()
            for button in content_body_zone_options:
                button.clicked.connect(partial(self.pass_content_body_zone, button))

        # When one of the Buttons within the "Content Body Area" is clicked, the READ process on the first DB will
        # happen, in function of the Body Area's option chosen, given that the Zone is already set to "Body" at this
        # stage
        if isinstance(self.get_current_main_window_content_view(), AccessDBPIIContentBodyAreaView):
            content_body_area_options = self.get_current_main_window_content_view().get_corresponding_hmi() \
                .get_content_body_area_options()
            for button in content_body_area_options:
                button.clicked.connect(partial(self.pass_content_area_zone, button))

        # When the "Button OK" of any Form for the Weight recording corresponding to the Category (Material)
        # is clicked, save the Input Text as the chosen Weight and pass to the next Form
        for view in self.get_forms_weights_materials_views():
            current_hmi = view.get_corresponding_hmi()
            current_hmi.get_button_ok().clicked.connect(
                partial(self.pass_form_weight, current_hmi.get_label_material().text())
            )

        form_weights_validation_view_ui = self.get_form_weights_validation_view().get_corresponding_hmi()
        if form_weights_validation_view_ui.get_form_weights_validation().isVisible():
            # When the "Button OK" of the Form for the Weights validation is clicked, proceed to the saving
            # of all the weights in DB and close the Form at the end of it
            form_weights_validation_view_ui.get_button_ok().clicked.connect(
                    self.save_weights
            )

            # When the "Button Nazad" of the Form for the Weights validation is clicked, go back to the
            # Aluminijum-related Form for another series of Weights insertion
            form_weights_validation_view_ui.get_button_nazad().clicked.connect(
                self.restart_weights_insertion
            )

    def pass_content_zone(self, button: QPushButton):
        """
        If the Button (Option) chosen is that of "Manufacturing", load the "Content Familijie".
        Otherwise ("Cutting" or "Lead Prep"), directly pass to the READ process on the first DB.
        :param button: The Button (Option) chosen by the User.
        :return: None
        """
        if button.text() == "Manufacturing":
            """
            "Manufacturing" option has been chosen, let's load the "Familijie Content" on the main window
            """
            # getting the main window
            main_window_view = self.get_accessdb_pii_main_window_view()
            # preparing the "Familijie Content"
            content_familijie_view = AccessDBPIIContentFamilijeView(
                main_window_view.get_corresponding_hmi().get_widget_content()
            )
            # loading the "Familijie Content"
            main_window_view.set_content_view(content_familijie_view)
            # formalizing the GUI's state transition
            self.set_current_main_window_content_view(content_familijie_view)
        else:
            """
            Another option different from "Manufacturing" has been chosen, therefore, directly to the READ process 
            on the first DB, the latter which is the first STEP of the Business Logic...
            """
            # The Label of the Option (Button) will serve as both the "Zone" and "Area" parameter
            parameter = button.text()
            self.launch_business_logic(parameter, parameter)
        # Since a transition of GUI's state has taken place, an update of the Events management is required
        self.manage_events()

    def pass_content_familije(self, button: QPushButton):
        """
        If the Button (Option) chosen is that of "Body", load the "Body Zone Content".
        Otherwise ("Cockpit", "Engine" or "Seats"), directly pass to the READ process on the first DB.
        :param button: The Button (Option) chosen by the User.
        :return: None
        """
        if button.text() == "Body":
            """
            "Body" option has been chosen, let's load the "Body Zone Content" on the main window
            """
            # getting the main window
            main_window_view = self.get_accessdb_pii_main_window_view()
            # preparing the "Body Zone Content"
            content_body_zone_view = AccessDBPIIContentBodyZoneView(
                main_window_view.get_corresponding_hmi().get_widget_content()
            )
            # loading the "Body Zone Content"
            main_window_view.set_content_view(content_body_zone_view)
            # formalizing the GUI's state transition
            self.set_current_main_window_content_view(content_body_zone_view)
        else:
            """
            Another option different from "Body" has been chosen, therefore, to the READ process directly, the latter 
            which is the first STEP of the Business Logic...
            """
            # The Label of the Option (Button) will serve as both the "Zone" and "Area" parameter
            parameter = button.text()
            self.launch_business_logic(parameter, parameter)
        # Since a transition of GUI's state has taken place, an update of the Events management is required
        self.manage_events()

    def pass_content_body_zone(self, button: QPushButton):
        """
        If the options chosen by the User content "SUB", the Content Body Area will be displayed.
        Otherwise, the User will be directly redirected to the READ process on the First DB.
        :param button: The button selected with the Content Body Zone
        :return: None
        """""
        if "SUB " in button.text():
            """
            A "SUB *" option has been chosen, let's load the "Body Area Content" on the main window
            """
            # getting the main window
            main_window_view = self.get_accessdb_pii_main_window_view()
            # preparing the "Body Area Content"
            content_body_area_view = AccessDBPIIContentBodyAreaView(
                main_window_view.get_corresponding_hmi().get_widget_content()
            )
            # storing the first Body Area selected for the next Sub-step
            first_area_selected = button.text().replace("SUB ", "")
            content_body_area_view.set_first_area_selected(first_area_selected)
            # loading the "Body Zone Content"
            main_window_view.set_content_view(content_body_area_view)
            # formalizing the GUI's state transition
            self.set_current_main_window_content_view(content_body_area_view)
        else:
            """
            Another option different from "SUB *" has been chosen, therefore, to the READ process directly, the latter 
            which is the first STEP of the Business Logic...
            """
            # The Label of the Option (Button) will serve as the "Area" parameter, whereas the "Zone" parameter  will
            # be set to "Body"
            area_parameter = button.text()
            self.launch_business_logic("Body", area_parameter)
        # Since a transition of GUI's state has taken place, an update of the Events management is required
        self.manage_events()

    def pass_content_area_zone(self, button: QPushButton):
        """
        Will launch the READ from the 1st DB with the combination of the first and current areas selected as the
        "Area" parameter
        :param button: The button (option) of second Area selected by the User
        :return: None
        """
        try:
            # Combining the First and the Second (the current one) Area selected to form the "Area" parameter for the
            # READ from the MFG Table, given that at this stage, it is already sure the the "Zone" parameter is
            # logically set to "Body"
            area_parameter_part_1 = self.get_current_main_window_content_view().get_first_area_selected()
            area_parameter_part_2 = button.text()
            area_parameter = area_parameter_part_1 + " - " + area_parameter_part_2
            self.launch_business_logic("Body", area_parameter)
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Transition of VIEW's state. "
            )
            raise

    def launch_business_logic(self, zone_parameter: str, area_parameter: str) -> list:
        """
        STEP 1: Launching the READ process related to MFG data with the parameters required for.
        STEP 2: Managing anything related to the Excel "Submition" file
        :param zone_parameter: The "Zone" parameter
        :param area_parameter: The "Area" parameter
        :return: The list of MFG Lines retrieved
        """
        try:
            # STEP 0a: Because the Business Logic has benn launched already, let's make the Main Window disabled,
            # until the next specification of new parameters
            self.get_accessdb_pii_main_window_view().get_corresponding_hmi().get_main_window().setDisabled(True)
            # STEP 0b: We are now sure the the current "Area" parameter is the definitive one... so..
            self.set_current_area_selected(area_parameter)
            # STEP 1: Launching the READ process related to MFG data with the parameters required for.
            lines_mfg = self.get_accessdb_pii_as().read_mfg_data(zone_parameter, area_parameter)
            if lines_mfg:
                # STEP 2: Managing anything related to the Excel "Submition" file
                self.manage_excel_submition(zone_parameter, area_parameter, lines_mfg)

                # STEP 3: Launching the Weight recording for each Category, and then confirming them
                self.launch_weights_recordings()

                # POST-ACTION : Now that we're sure that all of the MFG Lines previously retrieved from the MFG tables
                # have been used during the "Submition", we have to update their status in DB (to "read")
                for line in lines_mfg:
                    self.get_accessdb_pii_as().update_mfg_line_status(line.get_id())
            else:
                LOGGER.info(
                    "No MFG line corresponding to parameters zone : \"" + zone_parameter + "\" and area : \""
                    + area_parameter + "\" has been found."
                )
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the READ Command. "
            )
            raise

    def manage_excel_submition(self, zone_parameter: str, area_parameter: str, lines_mfg: list):
        """
        STEP A: Generating a second list from the MFG lines list, where the new lines are the combination of the old
        ones by their Category (Material);
        STEP B: Creating the Excel File for the "Submition"
        STEP C: Inserting all the compressed categorized lines within the newly-created Excel file
        STEP D: Printing the newly-fed Excel file
        :param zone_parameter: The "Zone" parameter chosen by the User through the sequence of GUIs
        :param area_parameter: The "Area" parameter chosen by the User through the sequence of GUIs
        :param lines_mfg: The list of MFG lines READ from the MFG Table in the first DB
        :return:
        """
        # First, let's get the selected "Team"
        team = self.get_accessdb_pii_main_window_view().get_corresponding_hmi().get_combo_box_teams().currentText()
        # STEP A: Generating a second list from the MFG lines list, where the new lines are the combination of the old
        #          ones by their Category (Material);
        try:
            raw_lines_excel_submition = []
            for line_mfg in lines_mfg:
                line_excel_submition = LineExcelSubmitionDO()
                line_excel_submition.set_category(line_mfg.get_material())
                line_excel_submition.set_material_id(line_mfg.get_item())
                line_excel_submition.set_quantity(line_mfg.get_quantity())
                raw_lines_excel_submition.append(line_excel_submition)
            # Categorizing each raw line of Excel Submition by their "Category"
            raw_lines_aluminium = []
            raw_lines_copper = []
            raw_lines_plastic = []
            raw_lines_terminal = []
            raw_lines_harness = []
            for line in raw_lines_excel_submition:
                if line.get_category() == "Aluminijum":
                    raw_lines_aluminium.append(line)
                elif line.get_category() == "Bakar":
                    raw_lines_copper.append(line)
                elif line.get_category() == "Plastika":
                    raw_lines_plastic.append(line)
                elif line.get_category() == "Terminal":
                    raw_lines_terminal.append(line)
                elif line.get_category() == "Harness":
                    raw_lines_harness.append(line)
                else:
                    # Category not (yet) recognized, hope will never end up here...
                    msg_error = "Category of the line : \"" + line + "\" not (yet) recognized."
                    LOGGER.error(msg_error)
                    raise Exception(msg_error)
            # Now, for each categorized raw lines of Excel Submition, let's combine the lines with the same
            # "Material ID" into a single line
            lines_aluminium = self.compress_categorized_raw_lines(raw_lines_aluminium)
            lines_copper = self.compress_categorized_raw_lines(raw_lines_copper)
            lines_plastic = self.compress_categorized_raw_lines(raw_lines_plastic)
            lines_terminal = self.compress_categorized_raw_lines(raw_lines_terminal)
            lines_harness = self.compress_categorized_raw_lines(raw_lines_harness)

            # STEP B: Creating the Excel File for the "Submition" with the "Zone" parameter
            excel_file_submition_path = self.get_excel_as().create_submition_excel_file(zone_parameter)

            # STEP C: Inserting all the compressed categorized lines within the newly-created Excel file
            self.get_excel_as().insert_categorized_lines(
                team, area_parameter, "Aluminium", lines_aluminium, excel_file_submition_path
            )
            self.get_excel_as().insert_categorized_lines(
                team, area_parameter, "Copper", lines_copper, excel_file_submition_path
            )
            self.get_excel_as().insert_categorized_lines(
                team, area_parameter, "Plastic", lines_plastic, excel_file_submition_path
            )
            self.get_excel_as().insert_categorized_lines(
                team, area_parameter, "Terminal", lines_terminal, excel_file_submition_path
            )
            self.get_excel_as().insert_categorized_lines(
                team, area_parameter, "Harness", lines_harness, excel_file_submition_path
            )

            # STEP D: Printing the newly-fed Excel file
            self.get_excel_as().print_excel_file(excel_file_submition_path)
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the management process. "
            )
            raise

    def compress_categorized_raw_lines(self, categorized_raw_lines: list) -> list:
        """
        Combining the Excel Submition lines with the same "Material ID" into a single line
        :param categorized_raw_lines: The list of raw lines to be Compressed
        :return: The compressed version of the list of raw lines provided in parameters
        """
        try:
            compressed_list = []
            category_id_marks = []
            for line in categorized_raw_lines:
                if line.get_material_id() in category_id_marks:
                    # The line's material ID is already present within the current version of the compressed list
                    current_compressed_list_element = [x for x in compressed_list
                                                         if x.get_material_id() == line.get_material_id()][0]
                    current_compressed_list_element_index = compressed_list.index(current_compressed_list_element)
                    # adding the Quantities
                    current_compressed_list_element.set_quantity(
                        current_compressed_list_element.get_quantity() + line.get_quantity()
                    )
                    compressed_list[current_compressed_list_element_index] = current_compressed_list_element
                else:
                    # No line having the same material ID as the current one is already present within the current
                    # version
                    # of the compressed list, let's add it and mark it
                    compressed_list.append(line)
                    category_id_marks.append(line.get_material_id())
            return compressed_list
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the compressing process. "
            )
            raise

    def launch_weights_recordings(self):
        """
        Launching the recording of Weights related to all the different Categories
        :return: None
        """
        # The recording of Weights starts with the Aluminium-related One
        self.set_current_weight_category(self.categories_labels[0])
        self.get_forms_weights_materials_views()[0].get_corresponding_hmi().show_hmi()

    def pass_form_weight(self, category: str):
        """
        Managing the transition between the Forms in charge of the Categories' Weights recording process
        :param category: The current category being processed
        :return: None
        """
        try:
            if category == self.categories_labels[0]:
                self.load_next_form_weight(0)
            elif category == self.categories_labels[1]:
                self.load_next_form_weight(1)
            elif category == self.categories_labels[2]:
                self.load_next_form_weight(2)
            elif category == self.categories_labels[3]:
                self.load_next_form_weight(3)
            elif category == self.categories_labels[4]:
                """
                Do not pass to a Form Weight anymore, instead we need to pass to the Validations of all the Weights
                by opening the corresponding Form,...
                """
                # ... but first, we still need to record the Weight entered by the User
                old_current_form_ui = self.get_forms_weights_materials_views()[4].get_corresponding_hmi()
                weight_entered = old_current_form_ui.get_input_text_weight().text()
                # In order to avoid redundancy of data recorded
                if len(self.get_current_recorded_weighs()) <= 4:
                    self.get_current_recorded_weighs().append(weight_entered)
                else:
                    self.get_current_recorded_weighs()[4] = weight_entered
                old_current_form_ui.close_hmi()

                # Now, it's time the confirm all the Weights previously recorded
                self.confirm_weights()
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Recording process. "
            )
            raise

    def load_next_form_weight(self, current_form_weight_index: int):
        """
        Loading the next Form for Weight recording from the current one.
        :param current_form_weight_index:  The index of the current Form in the pecific list
        :return: None
        """
        try:
            old_current_form_ui = self.get_forms_weights_materials_views()[current_form_weight_index]\
                                        .get_corresponding_hmi()
            # Recording the Weight entered by the User
            weight_entered = old_current_form_ui.get_input_text_weight().text()
            if len(self.get_current_recorded_weighs()) <= current_form_weight_index:
                self.get_current_recorded_weighs().append(weight_entered)
            else:
                self.get_current_recorded_weighs()[current_form_weight_index] = weight_entered
            # Closing the old current Form
            old_current_form_ui.close_hmi()
            # Loading the new Form
            new_current_form_ui = self.get_forms_weights_materials_views()[current_form_weight_index + 1]\
                                        .get_corresponding_hmi()
            new_current_form_ui.show_hmi()
            self.set_current_weight_category(self.categories_labels[current_form_weight_index + 1])
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Recording process. "
            )
            raise

    def confirm_weights(self):
        """
        Loading the confirmation process of all the Weights inserted by the User
        :return: None
        """
        try:
            form_weights_validation_view = self.get_form_weights_validation_view()

            # First, let's load all the Weights to be validated...
            form_weights_validation_view.feed_weights_to_confirm(self.get_current_recorded_weighs())
            # ... before displaying the Form for their confirmation
            form_weights_validation_view.get_corresponding_hmi().show_hmi()
            # Finally, an update of the Events Management is necessary given the several evolutions before arriving here
            self.manage_events()
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Confirmation process. "
            )
            raise

    def save_weights(self):
        """
        Saving all the Weights confirmed by the User
        :return: None
        """
        try:
            # Preparing the LineWeightsDO to be saved in DB
            line_weights_to_be_stored = LineWeightsDO()
            line_weights_to_be_stored.set_area(self.get_current_area_selected())
            validation_form = self.get_form_weights_validation_view().get_corresponding_hmi()
            aluminium_weight = validation_form.get_text_aluminijum().text()
            if len(aluminium_weight) > 0:
                line_weights_to_be_stored.set_aluminium_weight(decimal.Decimal(aluminium_weight.replace(",", ".")))
            copper_weight = validation_form.get_text_bakar().text()
            if len(copper_weight) > 0:
                line_weights_to_be_stored.set_copper_weight(decimal.Decimal(copper_weight.replace(",", ".")))
            plastic_weight = validation_form.get_text_plastika().text()
            if len(plastic_weight) > 0:
                line_weights_to_be_stored.set_plastic_weight(decimal.Decimal(plastic_weight.replace(",", ".")))
            terminal_weight = validation_form.get_text_terminali().text()
            if len(terminal_weight) > 0:
                line_weights_to_be_stored.set_terminal_weight(decimal.Decimal(terminal_weight.replace(",", ".")))
            harness_weight = validation_form.get_text_harness().text()
            if len(harness_weight) > 0:
                line_weights_to_be_stored.set_harness_weight(decimal.Decimal(harness_weight.replace(",", ".")))
            team = self.get_accessdb_pii_main_window_view().get_corresponding_hmi().get_combo_box_teams().currentText()
            if len(team) > 0:
                line_weights_to_be_stored.set_team(int(team))

            # It's time to save all the confirmed Weights
            if self.get_form_weights_validation_view().get_corresponding_hmi().get_form_weights_validation()\
                    .isVisible():
                self.get_accessdb_pii_as().save_line_weights(line_weights_to_be_stored)
                # At the end of the process, the Form for the Confirmation of the Weight has to be closed
                self.get_form_weights_validation_view().get_corresponding_hmi().close_hmi()
                # And we need to "Re-Start" again
                self.start_another_submition()
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Save process. "
            )
            raise

    def start_another_submition(self):
        """
        Everything is finished with the current Submition, let's start another one
        :return: None
        """
        try:
            main_window_view = self.get_accessdb_pii_main_window_view()
            # First of all, let us not forget to Enable the Main Window again
            main_window_view.get_corresponding_hmi().get_main_window().setEnabled(True)

            # "Content" Zone as the Main Window's content
            content_zone_view = AccessDBPIIContentZoneView(
                main_window_view.get_corresponding_hmi().get_widget_content()
            )
            self.get_accessdb_pii_main_window_view().set_content_view(
                content_zone_view
            )
            self.set_current_main_window_content_view(content_zone_view)
            # If a team is already selected within the Team ComboBox of the Main Window, let's notify the
            # "Content" Zone about it, in order to activate all of its Options Buttons.
            # Otherwise, wait for the selection of a new Team to activate them again.
            if main_window_view.get_corresponding_hmi().get_combo_box_teams().currentIndex() != -1:
                self.get_current_main_window_content_view().manage_notification_by_parent()

            # (Re-)Set current "Area" selected to None
            self.set_current_area_selected(None)

            # All the zone for the insertion of Weight for all the Categories within the corresponding Forms
            # to be cleared
            for view in self.get_forms_weights_materials_views():
                view.get_corresponding_hmi().get_input_text_weight().clear()

            # (Re-)update Events management
            self.manage_events()
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Re-Start process. "
            )
            raise

    def restart_weights_insertion(self):
        """
        Re-starting the process of Weights insertion corresponding to the different Categories (Materials)
        :return: None
        """
        try:
            # First of all, let's clear all the Insertion areas of all the Forms
            for view in self.get_forms_weights_materials_views():
                view.get_corresponding_hmi().get_input_text_weight().clear()

            # Now, let's close the Form for the Weights confirmation
            self.get_form_weights_validation_view().get_corresponding_hmi().close_hmi()

            # Finally, let's (re-)launching the Weights insertion
            self.launch_weights_recordings()
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Re-Launch process. "
            )
            raise













