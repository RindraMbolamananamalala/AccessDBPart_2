# -*- coding: utf-8 -*-

"""
access_db_view_.py: The python file dedicated to the "View" part of the MVC pattern implemented within the
"PRESENTATION" layer of the Project.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from functools import partial

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from CONFIGURATIONS.application_properties import get_application_property
from PRESENTATION.HMI.ui_AccessDB_main_window import Ui_MainWindow


class AccessDBView:

    def set_n(self, n:int):
        self.n = n

    def get_n(self) -> int:
        return self.n

    def set_list_of_left_buttons(self, list_of_left_buttons: list):
        self.list_of_left_buttons = list_of_left_buttons

    def get_list_of_left_buttons(self) -> list:
        return self.list_of_left_buttons

    def set_current_left_button_selected(self, current_left_button_selected: QPushButton):
        self.current_left_button_selected = current_left_button_selected

    def get_current_left_button_selected(self) -> QPushButton:
        return self.current_left_button_selected

    def set_window_ui(self, window_ui: Ui_MainWindow):
        """

        :param window_ui: The Ui_MainWindow to be managed by the Current View.
        :return: None
        """
        self.window_ui = window_ui

    def get_window_ui(self) -> Ui_MainWindow:
        """

        :return: The Ui_MainWindow managed by the Current View.
        """
        return self.window_ui

    def __init__(self, *args):
        if len(args) == 1:
            # window UI was provided
            self.set_window_ui(args[0])

            # Feeding Team & Kod Greske Combo Boxes
            self.feed_combo_box_team()
            self.feed_combo_box_kod_greske()

            # Initializing the value of N to 0 at the beginning
            self.set_n(0)
            self.get_window_ui().get_label_n().setText(str(self.get_n()))

            # Managing the selection protocol of all the Buttons located at the Left Part of the View (the one that
            # is selected turns into Orange)
            self.set_list_of_left_buttons([])
            self.get_list_of_left_buttons().append(self.get_window_ui().get_button_aluminijum())
            self.get_list_of_left_buttons().append(self.get_window_ui().get_button_bakar())
            self.get_list_of_left_buttons().append(self.get_window_ui().get_button_harness())
            self.get_list_of_left_buttons().append(self.get_window_ui().get_button_plastika())
            self.get_list_of_left_buttons().append(self.get_window_ui().get_button_terminal())
            for button in self.get_list_of_left_buttons():
                button.clicked.connect(partial(self.update_left_button_selection, button))

            # Management of Events
            self.manage_events()

    def update_left_button_selection(self, left_button_selected: QPushButton):
        """
        The button that is selected turns into Orange
        :param left_button_selected: The left button that is currently selected
        :return: None
        """
        # First, let's (re-)initialize the presentation of each left button
        for left_button in self.get_list_of_left_buttons():
            left_button.setStyleSheet(u"background-color: #1c2632;\n"
                                             "color: #adaeaf;\n"
                                             "border-radius: 10px;")
            if left_button.text() == "Aluminijum":
                left_button.move(17, Ui_MainWindow.button_aluminijum_normal_y_position)
            if left_button.text() == "Bakar":
                left_button.move(17, Ui_MainWindow.button_bakar_normal_y_position)
            if left_button.text() == "Harness":
                left_button.move(17, Ui_MainWindow.button_harness_normal_y_position)
            if left_button.text() == "Plastika":
                left_button.move(17, Ui_MainWindow.button_plastika_normal_y_position)
            if left_button.text() == "Terminal":
                left_button.move(17, Ui_MainWindow.button_terminal_normal_y_position)
            left_button.resize(210, 91)

        # Now, let's update  the color, size and position of the currently selected left button only..
        left_button_selected.setStyleSheet(
            "background-color: #f84018; "
            "color: #1c2632;"
            "border-radius: 10px;"
        )
        left_button_selected.resize(235, 95)
        left_button_selected.move(2, left_button_selected.geometry().y())

        # ... and remember these selected button
        self.set_current_left_button_selected(left_button_selected)

    def manage_events(self):
        """
        Managing all the events related to the Elements contained within the View part
        """
        # Increasing / Decreasing the N-number when the user click on +/-
        self.get_window_ui().get_button_plus().clicked.connect(self.increase_n)
        self.get_window_ui().get_button_minus().clicked.connect(self.decrease_n)

    def increase_n(self):
        """
        Increasing the value of N by 1.

        :return: None
        """
        if self.get_n() < 5:
            self.set_n(self.get_n() + 1)
        self.get_window_ui().get_label_n().setText(str(self.get_n()))

    def decrease_n(self):
        """
        Decreasing the value of N by 1.

        :return: None
        """
        if self.get_n() > 0:
            self.set_n(self.get_n() - 1)
        self.get_window_ui().get_label_n().setText(str(self.get_n()))

    def feed_combo_box_team(self):
        """
        Feeding the Combo Box dedicated to "Teams" with the corresponding values contained in the application.ini file.
        :return: None
        """
        teams_list = get_application_property("teams").split(",")
        for team in teams_list:
            self.get_window_ui().get_combo_box_team().addItem(team)

    def feed_combo_box_kod_greske(self):
        """
        Feeding the Combo Box dedicated to "Kod Greske" with the corresponding values contained in the application.ini
        file.
        :return: None
        """
        defects_list = get_application_property("defects").split(",")
        for defect_code in defects_list:
            self.get_window_ui().get_combo_box_kod_greske().addItem(defect_code)

    def clear_all_boxes(self):
        """
        Clearing all boxes, except that of "Team"
        :return:
        """
        window = self.get_window_ui()
        window.get_combo_box_stanica().setCurrentIndex(-1)
        window.get_combo_box_stanica().setEnabled(False)
        window.get_combo_box_predmet().setCurrentIndex(-1)
        window.get_combo_box_predmet().setEnabled(False)
        window.get_combo_box_kod_greske().setCurrentIndex(-1)
        window.get_combo_box_kod_greske().setEnabled(False)
        window.get_label_n().setText("0")
        window.get_button_plus().setEnabled(False)
        window.get_button_minus().setEnabled(False)
        self.set_current_left_button_selected(None)
        for button in self.get_list_of_left_buttons():
            button.setStyleSheet(u"background-color: #1c2632;\n"
                                             "color: #adaeaf;\n"
                                             "border-radius: 10px;")
            button.setEnabled(False)
            if button.text() == "Aluminijum":
                button.move(17, Ui_MainWindow.button_aluminijum_normal_y_position)
            if button.text() == "Bakar":
                button.move(17, Ui_MainWindow.button_bakar_normal_y_position)
            if button.text() == "Harness":
                button.move(17, Ui_MainWindow.button_harness_normal_y_position)
            if button.text() == "Plastika":
                button.move(17, Ui_MainWindow.button_plastika_normal_y_position)
            if button.text() == "Terminal":
                button.move(17, Ui_MainWindow.button_terminal_normal_y_position)
            button.resize(210, 91)
        window.get_button_potvrdi().setEnabled(False)
        window.get_button_potvrdi().setStyleSheet(u"background-color: gray;\n"
                                          "color: white;\n"
                                          "border : 5px solid ;\n"
                                          "border-radius: 25px;\n"
                                          "border-color: white;")