# -*- coding: utf-8 -*-

"""
accessdb_pii_controller.py: The python file dedicated to the "Controller" part of the MVC pattern implemented within
the "PRESENTATION" layer of the Project.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PRESENTATION.VIEW.accessdb_pii_main_window_view import AccessDBPIIMainWindowView

from PRESENTATION.VIEW.WIDGET.accessdb_pii_content_zone_view import AccessDBPIIContentZoneView


class AccessDBPIIController:

    def set_accessdb_pii_main_window_view(self, accessdb_pii_main_window_view: AccessDBPIIMainWindowView):
        self.accessdb_pii_main_window_view = accessdb_pii_main_window_view

    def get_accessdb_pii_main_window_view(self) -> AccessDBPIIMainWindowView:
        return self.accessdb_pii_main_window_view

    def __init__(self):
        # Initializing the AccessDB Part II's Main Window's VIEW
        self.set_accessdb_pii_main_window_view(AccessDBPIIMainWindowView())
        main_window_view = self.get_accessdb_pii_main_window_view()

        # The "Content Zone" will be the first Widget Content to be displayed at the beginning
        self.get_accessdb_pii_main_window_view().set_content_view(
            AccessDBPIIContentZoneView(main_window_view.get_corresponding_hmi().get_widget_content())
        )
