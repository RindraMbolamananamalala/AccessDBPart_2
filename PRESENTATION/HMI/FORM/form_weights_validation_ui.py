# -*- coding: utf-8 -*-

"""
form_weights_validation.py: The python file dedicated to the implementation of the "Form"  dedicated to the Validation
of a material's weights by the User.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PRESENTATION.HMI.accessdb_pii_hmi import AccessDBPIIHMI


class FormWeightsValidationUI(AccessDBPIIHMI):

    def show_hmi(self):
        """
        Displaying the form
        :return:
        """
        self.get_form_weights_validation().show()

    def close_hmi(self):
        """
        Closing the form
        :return:
        """
        self.get_form_weights_validation().close()

    def set_form_weights_validation(self, form_weights_validation: QWidget):
        """

        :param form_weights_validation: The main Widget of the From
        :return:
        """
        self.form_weights_validation = form_weights_validation

    def get_form_weights_validation(self) -> QWidget:
        """

        :return: The main Widget of the From
        """
        return self.form_weights_validation

    def get_text_aluminijum(self) -> QLineEdit:
        return self.text_aluminijium

    def get_text_bakar(self) -> QLineEdit:
        return self.text_bakar

    def get_text_plastika(self) -> QLineEdit:
        return self.text_plastika

    def get_text_terminali(self) -> QLineEdit:
        return self.text_terminali

    def get_text_harness(self) -> QLineEdit:
        return self.text_harness

    def get_button_ok(self) -> QPushButton:
        return self.button_ok

    def get_button_nazad(self) -> QPushButton:
        return self.button_nazad

    def __init__(self, parent: QWidget):
        # First, let's call the Superclass' __init__() function
        super(FormWeightsValidationUI, self).__init__()

        # Then, let's set up the current Form
        form_weights_validation = QWidget(parent)
        self.set_form_weights_validation(form_weights_validation)
        if not form_weights_validation.objectName():
            form_weights_validation.setObjectName(u"Form")
        form_weights_validation.setFixedSize(732, 526)
        form_weights_validation.setStyleSheet(u"background-color: #d2d2d2;\n"
                                              "border-radius: 25px;")
        self.label_finalna_potvrda = QLabel(form_weights_validation)
        self.label_finalna_potvrda.setObjectName(u"label_finalna_potvrda")
        self.label_finalna_potvrda.setGeometry(QRect(10, 10, 181, 31))
        font = QFont()
        font.setFamily(u"Century Gothic")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_finalna_potvrda.setFont(font)
        self.label_finalna_potvrda.setStyleSheet(u"color: #1c2632;")
        self.label_aluminijium = QLabel(form_weights_validation)
        self.label_aluminijium.setObjectName(u"label_aluminijium")
        self.label_aluminijium.setGeometry(QRect(30, 70, 211, 51))
        font1 = QFont()
        font1.setFamily(u"Yu Gothic UI Light")
        font1.setPointSize(25)
        self.label_aluminijium.setFont(font1)
        self.label_aluminijium.setStyleSheet(u"color: #1c2632;")
        self.text_aluminijium = QLineEdit(form_weights_validation)
        self.text_aluminijium.setAlignment(Qt.AlignCenter)
        self.text_aluminijium.setObjectName(u"text_aluminijium")
        self.text_aluminijium.setGeometry(QRect(260, 70, 271, 51))
        font2 = QFont()
        font2.setFamily(u"Century Gothic")
        font2.setPointSize(20)
        self.text_aluminijium.setFont(font2)
        self.text_aluminijium.setStyleSheet(u"border : 1px solid ;\n"
                                            "border-radius: 10px;\n"
                                            "border-color: #1c2632;\n"
                                            "background-color: #e5e5e5;")
        self.label_bakar = QLabel(form_weights_validation)
        self.label_bakar.setObjectName(u"label_bakar")
        self.label_bakar.setGeometry(QRect(30, 140, 211, 51))
        self.label_bakar.setFont(font1)
        self.label_bakar.setStyleSheet(u"color: #1c2632;")
        self.text_bakar = QLineEdit(form_weights_validation)
        self.text_bakar.setObjectName(u"text_bakar")
        self.text_bakar.setGeometry(QRect(260, 140, 271, 51))
        self.text_bakar.setAlignment(Qt.AlignCenter)
        self.text_bakar.setFont(font2)
        self.text_bakar.setStyleSheet(u"border : 1px solid ;\n"
                                      "border-radius: 10px;\n"
                                      "border-color: #1c2632;\n"
                                      "background-color: #e5e5e5;")
        self.label_terminali = QLabel(form_weights_validation)
        self.label_terminali.setObjectName(u"label_terminali")
        self.label_terminali.setGeometry(QRect(30, 280, 211, 51))
        self.label_terminali.setFont(font1)
        self.label_terminali.setStyleSheet(u"color: #1c2632;")
        self.label_plastika = QLabel(form_weights_validation)
        self.label_plastika.setObjectName(u"label_plastika")
        self.label_plastika.setGeometry(QRect(30, 210, 211, 51))
        self.label_plastika.setFont(font1)
        self.label_plastika.setStyleSheet(u"color: #1c2632;")
        self.text_plastika = QLineEdit(form_weights_validation)
        self.text_plastika.setObjectName(u"text_plastika")
        self.text_plastika.setGeometry(QRect(260, 210, 271, 51))
        self.text_plastika.setAlignment(Qt.AlignCenter)
        self.text_plastika.setFont(font2)
        self.text_plastika.setStyleSheet(u"border : 1px solid ;\n"
                                         "border-radius: 10px;\n"
                                         "border-color: #1c2632;\n"
                                         "background-color: #e5e5e5;")
        self.text_terminali = QLineEdit(form_weights_validation)
        self.text_terminali.setObjectName(u"text_terminali")
        self.text_terminali.setGeometry(QRect(260, 280, 271, 51))
        self.text_terminali.setFont(font2)
        self.text_terminali.setAlignment(Qt.AlignCenter)
        self.text_terminali.setStyleSheet(u"border : 1px solid ;\n"
                                          "border-radius: 10px;\n"
                                          "border-color: #1c2632;\n"
                                          "background-color: #e5e5e5;")
        self.text_harness = QLineEdit(form_weights_validation)
        self.text_harness.setObjectName(u"text_harness")
        self.text_harness.setGeometry(QRect(260, 350, 271, 51))
        self.text_harness.setFont(font2)
        self.text_harness.setAlignment(Qt.AlignCenter)
        self.text_harness.setStyleSheet(u"border : 1px solid ;\n"
                                        "border-radius: 10px;\n"
                                        "border-color: #1c2632;\n"
                                        "background-color: #e5e5e5;")
        self.label_harness = QLabel(form_weights_validation)
        self.label_harness.setObjectName(u"label_harness")
        self.label_harness.setGeometry(QRect(30, 350, 211, 51))
        self.label_harness.setFont(font1)
        self.label_harness.setStyleSheet(u"color: #1c2632;")
        self.button_ok = QPushButton(form_weights_validation)
        self.button_ok.setObjectName(u"button_ok")
        self.button_ok.setCursor(Qt.PointingHandCursor)
        self.button_ok.setGeometry(QRect(170, 430, 171, 61))
        font3 = QFont()
        font3.setFamily(u"Century Gothic")
        font3.setPointSize(13)
        self.button_ok.setFont(font3)
        self.button_ok.setStyleSheet(u"border-radius: 25px;\n"
                                     "background-color: #1c2632;\n"
                                     "color: #d2d2d2;")
        self.button_nazad = QPushButton(form_weights_validation)
        self.button_nazad.setObjectName(u"button_nazad")
        self.button_nazad.setGeometry(QRect(400, 430, 171, 61))
        self.button_nazad.setFont(font3)
        self.button_nazad.setCursor(Qt.PointingHandCursor)
        self.button_nazad.setStyleSheet(u"border-radius: 25px;\n"
                                        "background-color: #1c2632;\n"
                                        "color: #d2d2d2;")

        # Until further notice, let's make it not possible to force the Form to be exited via the "X" Button
        self.get_form_weights_validation().setWindowFlag(Qt.WindowCloseButtonHint, False)

        self.retranslateUi(form_weights_validation)

        QMetaObject.connectSlotsByName(form_weights_validation)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_finalna_potvrda.setText(QCoreApplication.translate("Form", u"Finalna potvrda", None))
        self.label_aluminijium.setText(QCoreApplication.translate("Form", u"Aluminijium", None))
        self.text_aluminijium.setPlaceholderText(QCoreApplication.translate("Form", u"kg", None))
        self.label_bakar.setText(QCoreApplication.translate("Form", u"Bakar", None))
        self.text_bakar.setPlaceholderText(QCoreApplication.translate("Form", u"kg", None))
        self.label_terminali.setText(QCoreApplication.translate("Form", u"Terminali", None))
        self.label_plastika.setText(QCoreApplication.translate("Form", u"Plastika", None))
        self.text_plastika.setPlaceholderText(QCoreApplication.translate("Form", u"kg", None))
        self.text_terminali.setPlaceholderText(QCoreApplication.translate("Form", u"kg", None))
        self.text_harness.setPlaceholderText(QCoreApplication.translate("Form", u"kg", None))
        self.label_harness.setText(QCoreApplication.translate("Form", u"Harness", None))
        self.button_ok.setText(QCoreApplication.translate("Form", u"OK", None))
        self.button_nazad.setText(QCoreApplication.translate("Form", u"Nazad", None))
    # retranslateUi
