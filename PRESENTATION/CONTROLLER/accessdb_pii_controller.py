# -*- coding: utf-8 -*-

"""
accessdb_pii_controller.py: The python file dedicated to the "Controller" part of the MVC pattern implemented within
the "PRESENTATION" layer of the Project.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from functools import partial

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


from PRESENTATION.VIEW.accessdb_pii_main_window_view import AccessDBPIIMainWindowView

from PRESENTATION.VIEW.WIDGET.accessdb_pii_content_view import AccessDBPIIContentView
from PRESENTATION.VIEW.WIDGET.accessdb_pii_content_zone_view import AccessDBPIIContentZoneView
from PRESENTATION.VIEW.WIDGET.accessdb_pii_content_familije_view import AccessDBPIIContentFamilijeView


class AccessDBPIIController:

    def set_accessdb_pii_main_window_view(self, accessdb_pii_main_window_view: AccessDBPIIMainWindowView):
        """

        :param accessdb_pii_main_window_view: The main window VIEW of the Application
        :return: None
        """
        self.accessdb_pii_main_window_view = accessdb_pii_main_window_view

    def get_accessdb_pii_main_window_view(self) -> AccessDBPIIMainWindowView:
        """

        :return: The main window VIEW of the Application
        """
        return self.accessdb_pii_main_window_view

    def set_current_main_window_content_view(self, current_main_window_content_view: AccessDBPIIContentView):
        """

        :param current_main_window_content_view:  The current content VIEW of the Main Window
        :return: None
        """
        self.current_main_window_content_view = current_main_window_content_view

    def get_current_main_window_content_view(self) -> AccessDBPIIContentView:
        """

        :return: The current content VIEW of the Main Window
        """
        return self.current_main_window_content_view

    def __init__(self):
        # Initializing the AccessDB Part II's Main Window's VIEW
        self.set_accessdb_pii_main_window_view(AccessDBPIIMainWindowView())
        main_window_view = self.get_accessdb_pii_main_window_view()

        # The "Content Zone" will be the first Widget Content to be displayed at the beginning
        content_zone_view = AccessDBPIIContentZoneView(main_window_view.get_corresponding_hmi().get_widget_content())
        self.get_accessdb_pii_main_window_view().set_content_view(
            content_zone_view
        )
        self.set_current_main_window_content_view(content_zone_view)

        # Managing the whole set of Events
        self.manage_events()

    def manage_events(self):
        """
        Managing all the set of Events related to the Application
        :return: None
        """

        # When one of the Buttons within the "Content Zone" is clicked, the user may have in visual the "Content
        # Familijie", or, the READ process on the first DB will directly happen, in function of the Zone's option chosen
        if isinstance(self.get_current_main_window_content_view(), AccessDBPIIContentZoneView):
            content_zone_options = self.get_current_main_window_content_view().get_corresponding_hmi()\
                                        .get_content_zone_options()
            for button in content_zone_options:
                button.clicked.connect(partial(self.pass_content_zone, button))

    def pass_content_zone(self, button: QPushButton):
        """
        If the Button (Option) chosen is that of "Manufacturing", load the "Content Familijie".
        Otherwise ("Cutting" or "Lead Prep"), directly pass to the READ process on the first DB.
        :param button: The Button (Option) chosen by the User.
        :return: None
        """
        if button.text() == "Manufacturing":
            """
            "Manufacturing" option has been chosen, let's load the "Familijie Content" on the main window
            """
            # getting the main window
            main_window_view = self.get_accessdb_pii_main_window_view()
            # preparing the "Familijie Content"
            content_familijie_view = AccessDBPIIContentFamilijeView(
                main_window_view.get_corresponding_hmi().get_widget_content()
            )
            # loading the "Familijie Content"
            main_window_view.set_content_view(content_familijie_view)
        else:
            """
            Another option different from "Manufacturing" has been chosen, therefore, directly to the READ process 
            on the first DB.
            """
            """TO BE MANAGED LATER, JUST PASS FOR THE MOMENT"""
            print(button.text() + " has been chosen, directly to READ process then!!!")
