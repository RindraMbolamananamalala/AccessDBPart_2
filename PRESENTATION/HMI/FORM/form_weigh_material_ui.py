# -*- coding: utf-8 -*-

"""
form_weigh_material_ui.py: The python file dedicated to the implementation of the "Form"  dedicated to the Input of
a material's weigh by the User.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PRESENTATION.HMI.accessdb_pii_hmi import AccessDBPIIHMI


class FormWeighMaterialUI(AccessDBPIIHMI):

    def show_hmi(self):
        """
        Displaying the Form.
        :return:
        """
        self.get_form_weigh_material().show()

    def set_form_weigh_material(self, form_weigh_material: QWidget):
        """

        :param form_weigh_material: The main Widget of the form
        :return:
        """
        self.form_weigh_material = form_weigh_material

    def get_form_weigh_material(self) -> QWidget:
        """

        :return: The main Widget of the form
        """
        return self.form_weigh_material

    def __init__(self, parent: QWidget):
        """

        :param parent: The Widget that plays the role of the Form
        """
        # First, let's call the Superclass' __init__() function
        super(FormWeighMaterialUI, self).__init__()

        # Then, let's set up the current Form
        form_weigh_material = QWidget(parent)
        self.set_form_weigh_material(form_weigh_material)
        if not form_weigh_material.objectName():
            form_weigh_material.setObjectName(u"form_weigh_material")
        form_weigh_material.resize(732, 314)
        form_weigh_material.setStyleSheet(u"background-color: #d2d2d2;\n"
                                          "border-radius: 25px;")
        self.label_unesi_tezinu = QLabel(form_weigh_material)
        self.label_unesi_tezinu.setObjectName(u"label_unesi_tezinu")
        self.label_unesi_tezinu.setGeometry(QRect(10, 10, 171, 31))
        font = QFont()
        font.setFamily(u"Century Gothic")
        font.setPointSize(14)
        self.label_unesi_tezinu.setFont(font)
        self.label_unesi_tezinu.setStyleSheet(u"color: #1c2632;")
        self.label_material = QLabel(form_weigh_material)
        self.label_material.setObjectName(u"label_material")
        self.label_material.setGeometry(QRect(180, 10, 191, 31))
        self.label_material.setFont(font)
        self.label_material.setStyleSheet(u"color: #1c2632;")
        self.input_text_weigh = QTextEdit(form_weigh_material)
        self.input_text_weigh.setObjectName(u"input_text_weigh")
        self.input_text_weigh.setGeometry(QRect(140, 90, 431, 101))
        self.input_text_weigh.setStyleSheet("")
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        font1.setPointSize(25)
        self.input_text_weigh.setFont(font1)
        self.input_text_weigh.setAlignment(Qt.AlignCenter)
        self.input_text_weigh.textChanged.connect(self.format_weigh_input)
        self.input_text_weigh.setStyleSheet(u"border : 1px solid ; background-color: #e5e5e5;"
                                            "border-radius: 25px;\n"
                                            "border-color: #1c2632;")
        self.button_ok = QPushButton(form_weigh_material)
        self.button_ok.setObjectName(u"button_ok")
        self.button_ok.setGeometry(QRect(270, 220, 171, 61))
        font2 = QFont()
        font2.setFamily(u"Century Gothic")
        font2.setPointSize(13)
        self.button_ok.setFont(font2)
        self.button_ok.setStyleSheet(u"border-radius: 25px;\n"
                                     "background-color: #1c2632;\n"
                                     "color: #d2d2d2;")

        self.retranslateUi(form_weigh_material)

        QMetaObject.connectSlotsByName(form_weigh_material)
    # setupUi

    def format_weigh_input(self):
        """
        Formatting the text provided by the User within the Input Text
        :return:
        """
        width = self.input_text_weigh.fontMetrics().width(self.input_text_weigh.toPlainText())
        self.input_text_weigh.setMinimumWidth(width)

    def retranslateUi(self, form_weigh_material):
        form_weigh_material.setWindowTitle(QCoreApplication.translate("form_weigh_material", u"Form", None))
        self.label_unesi_tezinu.setText(QCoreApplication.translate("form_weigh_material", u"Unesi tezinu za", None))
        self.label_material.setText(QCoreApplication.translate("form_weigh_material", u"bakar", None))
        self.input_text_weigh.setPlainText("")
        self.input_text_weigh.setPlaceholderText(QCoreApplication.translate("form_weigh_material", u"kg", None))
        self.button_ok.setText(QCoreApplication.translate("form_weigh_material", u"OK", None))
    # retranslateUi
