# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow_GUIYUWgVT.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

"""
accessdb_pii_main_window.py: The python file dedicated to the implementation of the GUI related to the Main Window of
the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from CONFIGURATIONS.application_properties import get_application_property
from CONFIGURATIONS.logger import LOGGER

from PRESENTATION.HMI.accessdb_pii_hmi import AccessDBPIIHMI

from PRESENTATION.HMI.WIDGET.accessdb_pii_content_zone import AccessDBPIIContentZone


class Ui_MainWindow(AccessDBPIIHMI):

    def show_hmi(self):
        """
        Displaying the main window.
        :return:
        """
        self.get_main_window().showMaximized()

    def set_main_window(self, main_window: QMainWindow):
        """

        :param main_window: The Qt Main Window to be used by the the current Main Window.
        :return:
        """
        self.main_window = main_window

    def get_main_window(self) -> QMainWindow:
        """

        :return: The Qt Main Window used by the the current Main Window.
        """
        return self.main_window

    def get_widget_content(self) -> QWidget:
        """

        :return: The Widget Content of the Main Window
        """
        return self.widget_content

    def set_content(self, content: AccessDBPIIContentZone):
        self.content = content

    def get_content(self) -> AccessDBPIIContentZone:
        return self.content

    def get_combo_box_teams(self) -> QComboBox:
        return self.combo_box_team

    def __init__(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.set_main_window(MainWindow)
        MainWindow.setFixedSize(1920, 1080)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 1920, 131))
        self.widget.setStyleSheet(u"background-color: #1c2632;")
        self.label_red = QLabel(self.widget)
        self.label_red.setObjectName(u"label_red")
        self.label_red.setGeometry(QRect(10, 10, 151, 71))
        font = QFont()
        font.setPointSize(40)
        self.label_red.setFont(font)
        self.label_red.setStyleSheet(u"color: #f7471f;")
        self.label_cage_scrap_submition = QLabel(self.widget)
        self.label_cage_scrap_submition.setObjectName(u"label_cage_scrap_submition")
        self.label_cage_scrap_submition.setGeometry(QRect(160, 10, 881, 71))
        self.label_cage_scrap_submition.setFont(font)
        self.label_cage_scrap_submition.setStyleSheet(u"color: #adaeaf;")
        self.combo_box_team = QComboBox(self.widget)
        self.combo_box_team.setObjectName(u"combo_box_team")
        self.combo_box_team.setGeometry(QRect(1360, 20, 241, 51))
        self.combo_box_team.setStyleSheet(u"background-color: #d2d2d2;\n"
"border-radius: 10px;\n"
"color: #393a46;\n"
"font-family: Century Gothic;\n"
"font-size: 30px;")
        self.label_logo = QLabel(self.widget)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setGeometry(QRect(1630, 20, 291, 51))
        self.label_logo.setPixmap(QPixmap(u"RESOURCES\\IMAGES\\logo_350x45_m75percent.png"))
        self.line_separation_header_content = QFrame(self.widget)
        self.line_separation_header_content.setObjectName(u"line_separation_header_content")
        self.line_separation_header_content.setGeometry(QRect(0, 95, 1920, 5))
        font1 = QFont()
        font1.setPointSize(5)
        self.line_separation_header_content.setFont(font1)
        self.line_separation_header_content.setAutoFillBackground(False)
        self.line_separation_header_content.setStyleSheet(u"background-color: #262f3d;")
        self.line_separation_header_content.setLineWidth(0)
        self.line_separation_header_content.setMidLineWidth(-16)
        self.line_separation_header_content.setFrameShape(QFrame.HLine)
        self.line_separation_header_content.setFrameShadow(QFrame.Sunken)
        self.widget_content = QWidget(self.centralwidget)
        self.widget_content.setObjectName(u"widget_content")
        self.widget_content.setGeometry(QRect(0, 100, 1920, 951))
        self.widget_content.setStyleSheet(u"background-color: #1c2632;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Feeding the "Teams" combobox and then choosing no "Team" at the beginning
        self.feed_team_combo_box()
        self.get_combo_box_teams().setCurrentIndex(-1)

        # Initializing the content of the MainWindow to None at the beginning
        self.content = None

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def feed_team_combo_box(self):
        """
        Feeding the Combo Box dedicated to "Teams" with the corresponding values contained in the application.ini file.
        :return: None
        """
        try:
            teams_list = get_application_property("teams").split(",")
            for team in teams_list:
                self.get_combo_box_teams().addItem(team)
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Feeding Process. "
            )
            raise

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_red.setText(QCoreApplication.translate("MainWindow", u"RED", None))
        self.label_cage_scrap_submition.setText(QCoreApplication.translate("MainWindow", u"CAGE SCRAP SUBMITION", None))
        self.label_logo.setText("")
    # retranslateUi

