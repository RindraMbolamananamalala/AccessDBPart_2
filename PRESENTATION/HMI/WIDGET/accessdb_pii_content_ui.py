# -*- coding: utf-8 -*-

"""
access_db_pii_content.py: The python file dedicated to the abstract definition of the Main Window's content area
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PRESENTATION.HMI.accessdb_pii_hmi import AccessDBPIIHMI


class AccessDBPIIContentUI(AccessDBPIIHMI):

    def show_hmi(self):
        """
        Displaying the widget content
        :return:
        """
        self.get_widget_content().show()

    def set_widget_content(self, widget_content: QWidget):
        """

        :param widget_content: The Widget dedicated to the Content
        :return: None
        """
        self.widget_content = widget_content

    def get_widget_content(self) -> QWidget:
        """

        :return: The Widget dedicated to the Content
        """
        return self.widget_content

    def __init__(self, parent: QWidget):
        """

        :param parent: The Widget that will play the role of "Parent" for the the Content
        """
        # First, let's call the Superclass' __init__() function
        super(AccessDBPIIContentUI, self).__init__()

        # Preparing the Widget Content
        widget_content = QWidget(parent)
        if not widget_content.objectName():
            widget_content.setObjectName(u"widget_content")
        self.set_widget_content(widget_content)
        widget_content.setStyleSheet(u"background-color: #1c2632;")

        # Management of the Label at the bottom dedicated to the description of the current kind of content
        self.label_bottom_description = QLabel(widget_content)
        self.label_bottom_description.setObjectName(u"label_bottom_descirption")
        self.label_bottom_description.setGeometry(QRect(40, 670, 1601, 230))
        font = QFont()
        font.setFamily(u"Yu Gothic UI Light")
        font.setPointSize(100)
        self.label_bottom_description.setFont(font)
        self.label_bottom_description.setStyleSheet(u"color: #adaeaf;")

        self.retranslateUi(widget_content)

        QMetaObject.connectSlotsByName(widget_content)
    # setupUi

    def retranslateUi(self, widget_content):
        """
        Retranslation of the Widget Content
        :param widget_content: The Widget Content to be retranslated
        :return: The retranslated version of the Widget Content provided as an argument
        """
        widget_content.setWindowTitle(QCoreApplication.translate("widget_content", u"Form", None))
    # retranslateUi
