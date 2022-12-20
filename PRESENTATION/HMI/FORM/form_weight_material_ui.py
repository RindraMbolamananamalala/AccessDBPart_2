# -*- coding: utf-8 -*-

"""
form_weight_material_ui.py: The python file dedicated to the implementation of the "Form"  dedicated to the Input of
a material's weight by the User.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PRESENTATION.HMI.accessdb_pii_hmi import AccessDBPIIHMI


class FormWeightMaterialUI(AccessDBPIIHMI):

    def show_hmi(self):
        """
        Displaying the Form.
        :return:
        """
        self.get_form_weight_material().setFocus()
        self.get_form_weight_material().show()

    def close_hmi(self):
        """
        Closing the From
        :return:
        """
        self.get_form_weight_material().close()

    def set_form_weight_material(self, form_weight_material: QWidget):
        """

        :param form_weight_material: The main Widget of the form
        :return:
        """
        self.form_weight_material = form_weight_material

    def get_form_weight_material(self) -> QWidget:
        """

        :return: The main Widget of the form
        """
        return self.form_weight_material

    def get_label_material(self) -> QLabel:
        return self.label_material

    def get_input_text_weight(self) -> QLineEdit:
        return self.input_text_weight

    def get_button_ok(self) -> QPushButton:
        return self.button_ok

    def __init__(self, parent: QWidget):
        """

        :param parent: The Widget that plays the role of the Form
        """
        # First, let's call the Superclass' __init__() function
        super(FormWeightMaterialUI, self).__init__()

        # Then, let's set up the current Form
        form_weight_material = QWidget(parent)
        self.set_form_weight_material(form_weight_material)
        if not form_weight_material.objectName():
            form_weight_material.setObjectName(u"form_weigh_material")
        form_weight_material.setFixedSize(732, 314)
        form_weight_material.setStyleSheet(u"background-color: #d2d2d2;\n"
                                           "border-radius: 25px;")
        self.label_unesi_tezinu = QLabel(form_weight_material)
        self.label_unesi_tezinu.setObjectName(u"label_unesi_tezinu")
        self.label_unesi_tezinu.setGeometry(QRect(10, 10, 171, 31))
        font = QFont()
        font.setFamily(u"Century Gothic")
        font.setPointSize(14)
        self.label_unesi_tezinu.setFont(font)
        self.label_unesi_tezinu.setStyleSheet(u"color: #1c2632;")
        self.label_material = QLabel(form_weight_material)
        self.label_material.setObjectName(u"label_material")
        self.label_material.setGeometry(QRect(180, 10, 191, 31))
        self.label_material.setFont(font)
        self.label_material.setStyleSheet(u"color: #1c2632;")
        self.input_text_weight = QLineEdit(form_weight_material)
        self.input_text_weight.setObjectName(u"input_text_weigh")
        self.input_text_weight.setGeometry(QRect(140, 90, 431, 101))
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        font1.setPointSize(25)
        self.input_text_weight.setFont(font1)
        self.input_text_weight.setAlignment(Qt.AlignCenter)
        input_text_wight_validator = QDoubleValidator()
        input_text_wight_validator.setNotation(QDoubleValidator.StandardNotation)
        input_text_wight_validator.setBottom(0.00)
        input_text_wight_validator.setDecimals(2)
        self.input_text_weight.setValidator(input_text_wight_validator)
        # regularizing the text input
        self.input_text_weight.textChanged.connect(self.regularize_weight_input)
        self.input_text_weight.setStyleSheet(u"border : 1px solid ; background-color: #e5e5e5;"
                                             "border-radius: 25px;\n"
                                             "border-color: #1c2632;")
        self.button_ok = QPushButton(form_weight_material)
        self.button_ok.setObjectName(u"button_ok")
        self.button_ok.setGeometry(QRect(270, 220, 171, 61))
        self.button_ok.setCursor(Qt.PointingHandCursor)
        font2 = QFont()
        font2.setFamily(u"Century Gothic")
        font2.setPointSize(13)
        self.button_ok.setFont(font2)
        self.button_ok.setStyleSheet(u"border-radius: 25px;\n"
                                     "background-color: #1c2632;\n"
                                     "color: #d2d2d2;")

        self.retranslateUi(form_weight_material)

        QMetaObject.connectSlotsByName(form_weight_material)

    # setupUi

    def regularize_weight_input(self):
        """
        Regularizing the format of the text provided by the User within the Input Text
        :return:
        """
        # If the text is a None one, replace it by 0,00
        text_to_be_regularized = self.get_input_text_weight().text()
        if len(text_to_be_regularized) < 1:
            self.get_input_text_weight().setText("0,00")

    def retranslateUi(self, form_weigh_material):
        form_weigh_material.setWindowTitle(QCoreApplication.translate("form_weigh_material", u"Form", None))
        self.label_unesi_tezinu.setText(QCoreApplication.translate("form_weigh_material", u"Unesi tezinu za", None))
        self.input_text_weight.setPlaceholderText("kg")
        self.input_text_weight.setPlaceholderText(QCoreApplication.translate("form_weigh_material", u"kg", None))
        self.button_ok.setText(QCoreApplication.translate("form_weigh_material", u"OK", None))
    # retranslateUi
