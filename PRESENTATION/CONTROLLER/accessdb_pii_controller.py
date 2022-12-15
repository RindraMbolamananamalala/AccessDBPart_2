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

from CONFIGURATIONS.logger import LOGGER

from PRESENTATION.VIEW.accessdb_pii_main_window_view import AccessDBPIIMainWindowView

from PRESENTATION.VIEW.WIDGET.accessdb_pii_content_view import AccessDBPIIContentView
from PRESENTATION.VIEW.WIDGET.accessdb_pii_content_zone_view import AccessDBPIIContentZoneView
from PRESENTATION.VIEW.WIDGET.accessdb_pii_content_familije_view import AccessDBPIIContentFamilijeView
from PRESENTATION.VIEW.WIDGET.accessdb_pii_content_body_zone_view import AccessDBPIIContentBodyZoneView
from PRESENTATION.VIEW.WIDGET.accessdb_pii_content_body_area_view import AccessDBPIIContentBodyAreaView

from BUSINESS.SERVICE.APPLICATION_SERVICE.INTF.accessdb_pii_as_intf import AccessDBPIIASIntf
from BUSINESS.SERVICE.APPLICATION_SERVICE.IMPL.accessdb_pii_as_impl import AccessDBPIIASImpl


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

    def set_accessdb_pii_as(self, accessdb_pii_as: AccessDBPIIASIntf):
        """

        :param accessdb_pii_as: The Access DB Part II general Application Service object to be used by the Controller
        :return: None
        """
        self.accessdb_pii_as = accessdb_pii_as

    def get_accessdb_pii_as(self) -> AccessDBPIIASIntf:
        """

        :return: The Access DB Part II general Application Service object used by the Controller
        """
        return self.accessdb_pii_as

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

        # Initializing all the ASs to be used by the Controller
        self.set_accessdb_pii_as(AccessDBPIIASImpl())

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
        # Familije", or, the READ process on the first DB will directly happen, in function of the Zone's option chosen
        if isinstance(self.get_current_main_window_content_view(), AccessDBPIIContentZoneView):
            content_zone_options = self.get_current_main_window_content_view().get_corresponding_hmi() \
                .get_content_zone_options()
            for button in content_zone_options:
                button.clicked.connect(partial(self.pass_content_zone, button))

        # When one of the Buttons within the "Content Familije" is clicked, the user may have in visual the "Body zone",
        # or, the READ process on the first DB will directly happen, in function of the Familije's option chosen
        if isinstance(self.get_current_main_window_content_view(), AccessDBPIIContentFamilijeView):
            content_familije_options = self.get_current_main_window_content_view().get_corresponding_hmi() \
                .get_content_familije_options()
            for button in content_familije_options:
                button.clicked.connect(partial(self.pass_content_familije, button))

        # When one of the Buttons within the "Content Body Zone" is clicked, the user may have in visual the
        # "Body area", or, the READ process on the first DB will directly happen, in function of the
        # Body Zone's option chosen
        if isinstance(self.get_current_main_window_content_view(), AccessDBPIIContentBodyZoneView):
            content_body_zone_options = self.get_current_main_window_content_view().get_corresponding_hmi() \
                .get_content_body_zone_options()
            for button in content_body_zone_options:
                button.clicked.connect(partial(self.pass_content_body_zone, button))

        # When one of the Buttons within the "Content Body Area" is clicked, the READ process on the first DB will
        # happen, in function of the Body Area's option chosen, given that the Zone is already set to "Body" at this
        # stage
        if isinstance(self.get_current_main_window_content_view(), AccessDBPIIContentBodyAreaView):
            content_body_area_options = self.get_current_main_window_content_view().get_corresponding_hmi() \
                .get_content_body_area_options()
            for button in content_body_area_options:
                button.clicked.connect(partial(self.pass_content_area_zone, button))

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
            # formalizing the GUI's state transition
            self.set_current_main_window_content_view(content_familijie_view)
        else:
            """
            Another option different from "Manufacturing" has been chosen, therefore, directly to the READ process 
            on the first DB, the latter which is the first STEP of the Business Logic...
            """
            # The Label of the Option (Button) will serve as both the "Zone" and "Area" parameter
            parameter = button.text()
            self.launch_business_logic(parameter, parameter)
        # Since a transition of GUI's state has taken place, an update of the Events management is required
        self.manage_events()

    def pass_content_familije(self, button: QPushButton):
        """
        If the Button (Option) chosen is that of "Body", load the "Body Zone Content".
        Otherwise ("Cockpit", "Engine" or "Seats"), directly pass to the READ process on the first DB.
        :param button: The Button (Option) chosen by the User.
        :return: None
        """
        if button.text() == "Body":
            """
            "Body" option has been chosen, let's load the "Body Zone Content" on the main window
            """
            # getting the main window
            main_window_view = self.get_accessdb_pii_main_window_view()
            # preparing the "Body Zone Content"
            content_body_zone_view = AccessDBPIIContentBodyZoneView(
                main_window_view.get_corresponding_hmi().get_widget_content()
            )
            # loading the "Body Zone Content"
            main_window_view.set_content_view(content_body_zone_view)
            # formalizing the GUI's state transition
            self.set_current_main_window_content_view(content_body_zone_view)
        else:
            """
            Another option different from "Body" has been chosen, therefore, to the READ process directly, the latter 
            which is the first STEP of the Business Logic...
            """
            # The Label of the Option (Button) will serve as both the "Zone" and "Area" parameter
            parameter = button.text()
            self.launch_business_logic(parameter, parameter)
        # Since a transition of GUI's state has taken place, an update of the Events management is required
        self.manage_events()

    def pass_content_body_zone(self, button: QPushButton):
        """
        If the options chosen by the User content "SUB", the Content Body Area will be displayed.
        Otherwise, the User will be directly redirected to the READ process on the First DB.
        :param button: The button selected with the Content Body Zone
        :return: None
        """""
        if "SUB " in button.text():
            """
            A "SUB *" option has been chosen, let's load the "Body Area Content" on the main window
            """
            # getting the main window
            main_window_view = self.get_accessdb_pii_main_window_view()
            # preparing the "Body Area Content"
            content_body_area_view = AccessDBPIIContentBodyAreaView(
                main_window_view.get_corresponding_hmi().get_widget_content()
            )
            # storing the first Body Area selected for the next Sub-step
            first_area_selected = button.text().replace("SUB ", "")
            content_body_area_view.set_first_area_selected(first_area_selected)
            # loading the "Body Zone Content"
            main_window_view.set_content_view(content_body_area_view)
            # formalizing the GUI's state transition
            self.set_current_main_window_content_view(content_body_area_view)
        else:
            """
            Another option different from "SUB *" has been chosen, therefore, to the READ process directly, the latter 
            which is the first STEP of the Business Logic...
            """
            # The Label of the Option (Button) will serve as the "Area" parameter, whereas the "Zone" parameter  will
            # be set to "Body"
            area_parameter = button.text()
            self.launch_business_logic("Body", area_parameter)
        # Since a transition of GUI's state has taken place, an update of the Events management is required
        self.manage_events()

    def pass_content_area_zone(self, button: QPushButton):
        """
        Will launch the READ from the 1st DB with the combination of the first and current areas selected as the
        "Area" parameter
        :param button: The button (option) of second Area selected by the User
        :return: None
        """
        try:
            # Combining the First and the Second (the current one) Area selected to form the "Area" parameter for the
            # READ from the MFG Table, given that at this stage, it is already sure the the "Zone" parameter is
            # logically set to "Body"
            area_parameter_part_1 = self.get_current_main_window_content_view().get_first_area_selected()
            area_parameter_part_2 = button.text()
            area_parameter = area_parameter_part_1 + " - " + area_parameter_part_2
            self.launch_business_logic("Body", area_parameter)
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Transition of VIEW's state. "
            )
            raise

    def launch_business_logic(self, zone_parameter: str, area_parameter: str) -> list:
        """
        STEP 1: Launching the READ process related to MFG data with the parameters required for.
        :param zone_parameter: The "Zone" parameter
        :param area_parameter: The "Area" parameter
        :return: The list of MFG Lines retrieved
        """
        try:
            # STEP 1
            lines_mfg = self.get_accessdb_pii_as().read_mfg_data(zone_parameter, area_parameter)
            if lines_mfg:
                for line_mfg in lines_mfg:
                    print(line_mfg)
                """
                ... and then, let's manage the Excel for the "Sumbmition"
                """
                self.manage_excel_submition()
            else:
                LOGGER.info(
                    "No MFG line corresponding to parameters zone : \"" + zone_parameter + "\" and area : \""
                    + area_parameter + "\" has been found."
                )
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the READ Command. "
            )
            raise

    def manage_excel_submition(self):
        # Just pass for the now, will be managed latter
        pass
