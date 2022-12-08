# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_Window_UImuDZFt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.examples.corelib.tools.codecs.codecs import MainWindow



class Ui_MainWindow(object):

    button_aluminijum_normal_y_position = 185
    button_bakar_normal_y_position = 295
    button_harness_normal_y_position = 405
    button_plastika_normal_y_position = 515
    button_terminal_normal_y_position = 625

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

    def get_button_aluminijum(self) -> QPushButton:
        return self.button_aluminijum

    def get_button_bakar(self) -> QPushButton:
        return self.button_bakar

    def get_button_harness(self) -> QPushButton:
        return self.button_harness

    def get_button_plastika(self) -> QPushButton:
        return self.button_plastika

    def get_button_terminal(self) -> QPushButton:
        return self.button_terminal

    def get_button_potvrdi(self) -> QPushButton:
        return self.button_potvrdi

    def get_combo_box_stanica(self) -> QComboBox:
        return self.combo_box_stanica

    def get_combo_box_predmet(self) -> QComboBox:
        return self.combo_box_predmet

    def get_combo_box_kod_greske(self) -> QComboBox:
        return self.combo_box_kod_greske

    def get_combo_box_team(self) -> QComboBox:
        return self.combo_box_team

    def get_combo_box_team(self) -> QComboBox:
        return self.combo_box_team

    def get_button_plus(self) -> QPushButton:
        return self.button_plus

    def get_button_minus(self) -> QPushButton:
        return self.button_minus

    def get_label_n(self) -> QLabel:
        return self.label_n

    def get_label_post_process(self)-> QLabel:
        return self.label_post_process

    def __init__(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.set_main_window(MainWindow)
        MainWindow.setFixedSize(1920, 1080)
        MainWindow.setStyleSheet(u"background-color: #d2d2d2;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget_window_left_part = QWidget(self.centralwidget)
        self.widget_window_left_part.setObjectName(u"widget_window_left_part")
        self.widget_window_left_part.setGeometry(QRect(0, 0, 241, 1080))
        self.widget_window_left_part.setStyleSheet(u"background-color: #d2d2d2;")
        self.label_scrap = QLabel(self.widget_window_left_part)
        self.label_scrap.setObjectName(u"label_scrap")
        self.label_scrap.setGeometry(QRect(10, 0, 220, 71))
        font = QFont()
        font.setPointSize(40)
        self.label_scrap.setFont(font)
        self.label_scrap.setStyleSheet(u"color: #f7471f;")
        self.label_scrap.setAlignment(Qt.AlignHCenter)
        self.button_aluminijum = QPushButton(self.widget_window_left_part)
        self.button_aluminijum.setCursor(Qt.PointingHandCursor)
        self.button_aluminijum.setObjectName(u"button_aluminijum")
        self.button_aluminijum.setGeometry(QRect(17, 185, 210, 91))
        font1 = QFont()
        font1.setPointSize(22)
        font1.setFamily(u"Century Gothic")
        font1.setBold(False)
        self.button_aluminijum.setFont(font1)
        self.button_aluminijum.setStyleSheet(u"background-color: #1c2632;\n"
                                             "color: #adaeaf;\n"
                                             "border-radius: 10px;")
        self.button_bakar = QPushButton(self.widget_window_left_part)
        self.button_bakar.setCursor(Qt.PointingHandCursor)
        self.button_bakar.setObjectName(u"button_bakar")
        self.button_bakar.setGeometry(QRect(17, 295, 210, 91))
        self.button_bakar.setFont(font1)
        self.button_bakar.setStyleSheet(u"background-color: #1c2632;\n"
                                        "color: #adaeaf;\n"
                                        "border-radius: 10px;")
        self.button_harness = QPushButton(self.widget_window_left_part)
        self.button_harness.setCursor(Qt.PointingHandCursor)
        self.button_harness.setObjectName(u"button_harness")
        self.button_harness.setGeometry(QRect(17, 405, 210, 91))
        self.button_harness.setFont(font1)
        self.button_harness.setStyleSheet(u"background-color: #1c2632;\n"
                                          "color: #adaeaf;\n"
                                          "border-radius: 10px;")
        self.button_plastika = QPushButton(self.widget_window_left_part)
        self.button_plastika.setCursor(Qt.PointingHandCursor)
        self.button_plastika.setObjectName(u"button_plastika")
        self.button_plastika.setGeometry(QRect(17, 515, 210, 91))
        self.button_plastika.setFont(font1)
        self.button_plastika.setStyleSheet(u"background-color: #1c2632;\n"
                                           "color: #adaeaf;\n"
                                           "border-radius: 10px;")
        self.button_terminal = QPushButton(self.widget_window_left_part)
        self.button_terminal.setCursor(Qt.PointingHandCursor)
        self.button_terminal.setObjectName(u"button_terminal")
        self.button_terminal.setGeometry(QRect(17, 625, 210, 91))
        self.button_terminal.setFont(font1)
        self.button_terminal.setStyleSheet(u"background-color: #1c2632;\n"
                                           "color: #adaeaf;\n"
                                           "border-radius: 10px;")
        self.button_potvrdi = QPushButton(self.widget_window_left_part)
        self.button_potvrdi.setCursor(Qt.PointingHandCursor)
        self.button_potvrdi.setObjectName(u"button_potvrdi")
        self.button_potvrdi.setGeometry(QRect(10, 800, 210, 171))
        font2 = QFont()
        font2.setPointSize(24)
        self.button_potvrdi.setFont(font2)
        self.button_potvrdi.setStyleSheet(u"background-color: #1c2632;\n"
                                          "color: #f7471f;\n"
                                          "border : 5px solid ;\n"
                                          "border-radius: 25px;\n"
                                          "border-color: #f7471f;")
        self.widget_window_right_part = QWidget(self.centralwidget)
        self.widget_window_right_part.setObjectName(u"widget_window_right_part")
        self.widget_window_right_part.setGeometry(QRect(240, 0, 1681, 1080))
        self.widget_window_right_part.setFont(font1)
        self.widget_window_right_part.setStyleSheet(u"background-color: #1c2632;\n"
                                                    "border-radius: 25px;")
        self.label_data_collector = QLabel(self.widget_window_right_part)
        self.label_data_collector.setObjectName(u"label_data_collector")
        self.label_data_collector.setGeometry(QRect(20, 0, 550, 71))
        self.label_data_collector.setFont(font)
        self.label_data_collector.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.label_data_collector.setStyleSheet(u"color: #adaeaf; border-radius: 0px;")
        self.label_logo = QLabel(self.widget_window_right_part)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setGeometry(QRect(1400, 10, 271, 51))
        self.label_logo.setPixmap(QPixmap(u"RESOURCES\\IMAGES\\logo_350x45_m75percent.png"))
        self.combo_box_team = QComboBox(self.widget_window_right_part)
        self.combo_box_team.setCursor(Qt.PointingHandCursor)
        self.combo_box_team.setObjectName(u"combo_box_team")
        self.combo_box_team.setGeometry(QRect(1400, 80, 261, 41))
        self.combo_box_team.setStyleSheet(u"background-color: #d2d2d2;"
                                            "color: #393a46;"
                                             "font-family: Century Gothic;"
                                             "font-size: 30px;")
        font_rights_label = QFont()
        font_rights_label.setPointSize(15)
        self.label_stanica = QLabel(self.widget_window_right_part)
        self.label_stanica.setObjectName(u"label_stanica")
        self.label_stanica.setGeometry(QRect(50, 140, 141, 31))
        self.label_stanica.setFont(font_rights_label)
        self.label_stanica.setStyleSheet(u"color: #adaeaf;")
        self.label_predmet = QLabel(self.widget_window_right_part)
        self.label_predmet.setObjectName(u"label_predmet")
        self.label_predmet.setGeometry(QRect(490, 140, 141, 31))
        self.label_predmet.setFont(font_rights_label)
        self.label_predmet.setStyleSheet(u"color: #adaeaf;")
        self.label_kod_greske = QLabel(self.widget_window_right_part)
        self.label_kod_greske.setObjectName(u"label_kod_greske")
        self.label_kod_greske.setGeometry(QRect(930, 130, 401, 31))
        self.label_kod_greske.setFont(font_rights_label)
        self.label_kod_greske.setStyleSheet(u"color: #adaeaf;")
        self.combo_box_stanica = QComboBox(self.widget_window_right_part)
        self.combo_box_stanica.setCursor(Qt.PointingHandCursor)
        self.combo_box_stanica.setObjectName(u"combo_box_stanica")
        self.combo_box_stanica.setGeometry(QRect(50, 190, 401, 61))
        self.combo_box_stanica.setStyleSheet(u"background-color: #d2d2d2;"
                                             "border-radius: 10px;"
                                             "color: #393a46;"
                                             "font-family: Century Gothic;"
                                             "font-size: 30px;")
        self.combo_box_predmet = QComboBox(self.widget_window_right_part)
        self.combo_box_predmet.setCursor(Qt.PointingHandCursor)
        self.combo_box_predmet.setObjectName(u"combo_box_predmet")
        self.combo_box_predmet.setGeometry(QRect(490, 190, 401, 61))
        self.combo_box_predmet.setStyleSheet(u"background-color: #d2d2d2;"
                                             "border-radius: 10px;"
                                             "color: #393a46;"
                                             "font-family: Century Gothic;"
                                             "font-size: 30px;")
        self.combo_box_kod_greske = QComboBox(self.widget_window_right_part)
        self.combo_box_kod_greske.setCursor(Qt.PointingHandCursor)
        self.combo_box_kod_greske.setObjectName(u"combo_box_kod_greske")
        self.combo_box_kod_greske.setGeometry(QRect(930, 190, 401, 61))
        self.combo_box_kod_greske.setStyleSheet(u"background-color: #d2d2d2;"
                                             "border-radius: 10px;"
                                             "color: #393a46;"
                                             "font-family: Century Gothic;"
                                             "font-size: 30px;")
        self.button_plus = QPushButton(self.widget_window_right_part)
        self.button_plus.setCursor(Qt.PointingHandCursor)
        self.button_plus.setObjectName(u"button_plus")
        self.button_plus.setGeometry(QRect(1470, 170, 121, 121))
        font3 = QFont()
        font3.setPointSize(100)
        self.button_plus.setFont(font3)
        self.button_plus.setLayoutDirection(Qt.LeftToRight)
        self.button_plus.setStyleSheet(u"color: #adaeaf;")
        self.button_minus = QPushButton(self.widget_window_right_part)
        self.button_minus.setCursor(Qt.PointingHandCursor)
        self.button_minus.setObjectName(u"button_minus")
        self.button_minus.setGeometry(QRect(1480, 610, 121, 61))
        self.button_minus.setFont(font3)
        self.button_minus.setLayoutDirection(Qt.LeftToRight)
        self.button_minus.setStyleSheet(u"color: #adaeaf;")
        self.label_n = QLabel(self.widget_window_right_part)
        self.label_n.setObjectName(u"label")
        self.label_n.setGeometry(QRect(1480, 330, 121, 271))
        self.label_n.setAlignment(Qt.AlignCenter)
        self.label_n.setFont(font3)
        self.label_n.setStyleSheet(u"background-color: #adaeaf;\n"
                                   "color: #1c2632;")
        self.label_post_process = QLabel(self.widget_window_right_part)
        self.label_post_process.setObjectName(u"label_post_process")
        self.label_post_process.setGeometry(QRect(60, 750, 1551, 211))
        font4 = QFont()
        font4.setPointSize(150)
        self.label_post_process.setFont(font4)
        self.label_post_process.setStyleSheet(u"color: #adaeaf;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_scrap.setText(QCoreApplication.translate("MainWindow", u"SCRAP", None))
        self.button_aluminijum.setText(QCoreApplication.translate("MainWindow", u"Aluminijum", None))
        self.button_bakar.setText(QCoreApplication.translate("MainWindow", u"Bakar", None))
        self.button_harness.setText(QCoreApplication.translate("MainWindow", u"Harness", None))
        self.button_plastika.setText(QCoreApplication.translate("MainWindow", u"Plastika", None))
        self.button_terminal.setText(QCoreApplication.translate("MainWindow", u"Terminal", None))
        self.button_potvrdi.setText(QCoreApplication.translate("MainWindow", u"Potvrdi", None))
        self.label_data_collector.setText(QCoreApplication.translate("MainWindow", u"DATA COLLECTOR", None))
        self.label_logo.setText("")
        self.label_stanica.setText(QCoreApplication.translate("MainWindow", u"Stanica", None))
        self.label_predmet.setText(QCoreApplication.translate("MainWindow", u"Predmet", None))
        self.label_kod_greske.setText(QCoreApplication.translate("MainWindow", u"Kod greske", None))
        self.button_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.button_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_n.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.label_post_process.setText(QCoreApplication.translate("MainWindow", u"Post Process", None))
    # retranslateUi
