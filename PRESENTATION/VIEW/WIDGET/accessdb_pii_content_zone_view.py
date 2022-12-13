# -*- coding: utf-8 -*-

"""
accessdb_pii_content_zone_view.py: The python file dedicated to the implementation of the VIEW:ContentZone  of
the Application, part of the implementation of the MVC pattern within the latter.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PRESENTATION.HMI.WIDGET.accessdb_pii_content_zone import AccessDBPIIContentZone

from PRESENTATION.VIEW.WIDGET.accessdb_pii_content_view import AccessDBPIIContentView

from PySide2.QtWidgets import *


class AccessDBPIIContentZoneView(AccessDBPIIContentView):

    def manage_notification_by_parent(self):
        """
        Managing the notification from the Parent reception
        :return: None
        """
        # Activating the Content Zone's options (buttons)
        for button in self.get_corresponding_hmi().get_content_zone_options():
            button.setEnabled(True)

    def __init__(self, parent: QWidget):
        #  First, let's call the Superclass' __init__() function
        super(AccessDBPIIContentZoneView, self).__init__()

        # and then, let's associate the View with an AccessDB Part II's Zone content UI
        self.set_corresponding_hmi(AccessDBPIIContentZone(parent))

        # now, at first, let's disable all the buttons corresponding to the Content Zone's options, waiting for
        # a "Team" selection within the dedicated combobox, at the level of the Parent
        for button in self.get_corresponding_hmi().get_content_zone_options():
            button.setDisabled(True)

