# -*- coding: utf-8 -*-

"""
accessdb_pii_main_window_view_.py: The python file dedicated to the "View:MainWindow" part of the MVC pattern
implemented within the "PRESENTATION" layer of the Project.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"


from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from CONFIGURATIONS.logger import LOGGER

from PRESENTATION.HMI.accessdb_pii_main_window_ui import Ui_MainWindow
from PRESENTATION.VIEW.accessdb_pii_view import AccessDBPIIView
from PRESENTATION.VIEW.WIDGET.accessdb_pii_content_view import AccessDBPIIContentView


class AccessDBPIIMainWindowView(AccessDBPIIView):

    def set_content_view(self, content_view: AccessDBPIIContentView):
        """
        The Main Widow VIEW has to be associated with a Content View in order to display a content:
        :param content_view: The Content View associated with the Main Window View
        :return:
        """
        self.content_view = content_view
        try:
            # And also, let's display the HMI associated with the Content View
            self.get_content_view().get_corresponding_hmi().show_hmi()
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Displaying Process. "
            )
            raise

    def get_content_view(self) -> AccessDBPIIContentView:
        """

        :return: he Content View associated with the Main Window View
        """
        return self.content_view

    def __init__(self):
        # Initializing the UI of the AccessDB Part II : The MainWindowUI
        self.set_corresponding_hmi(Ui_MainWindow(QMainWindow()))
