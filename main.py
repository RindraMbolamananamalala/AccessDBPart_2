# -*- coding: utf-8 -*-

"""
main.py: The python file in charge of the Launch of the whole App
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

import sys


from PySide2.QtWidgets import *


from PRESENTATION.CONTROLLER.accessdb_pii_controller import AccessDBPIIController

if __name__ == '__main__':
    application = QApplication(sys.argv)
    # Preparing the Controller
    controller = AccessDBPIIController()
    # Displaying the Main Window of the Application
    controller.get_accessdb_pii_main_window_view().get_corresponding_hmi().get_main_window().showMaximized()
    sys.exit(application.exec_())
