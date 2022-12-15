# -*- coding: utf-8 -*-

"""
accessdb_pii_content_body_area_view.py: The python file dedicated to the implementation of the VIEW:ContentBodyArea  of
the Application, part of the implementation of the MVC pattern within the latter.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PRESENTATION.HMI.WIDGET.accessdb_pii_content_body_area import AccessDBPIIContentBodyArea

from PRESENTATION.VIEW.WIDGET.accessdb_pii_content_view import AccessDBPIIContentView

from PySide2.QtWidgets import *


class AccessDBPIIContentBodyAreaView(AccessDBPIIContentView):

    def set_first_area_selected(self, first_area_selected: str):
        """

        :param first_area_selected: The first Area selected at the level of the Body Zone View
        :return: None
        """
        self.first_area_selected = first_area_selected

    def get_first_area_selected(self) -> str:
        """

        :return: The first Area selected at the level of the Body Zone View
        """
        return self.first_area_selected

    def __init__(self, parent: QWidget):
        #  First, let's call the Superclass' __init__() function
        super(AccessDBPIIContentBodyAreaView, self).__init__()

        # and then, let's associate the View with an AccessDB Part II's Zone content UI
        self.set_corresponding_hmi(AccessDBPIIContentBodyArea(parent))


