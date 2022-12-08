import sys
import time

from PySide2.QtWidgets import *

from PRESENTATION.HMI.ui_AccessDB_main_window import Ui_MainWindow
from PRESENTATION.VIEW.access_db_view import AccessDBView
from PRESENTATION.CONTROLLER.access_db_controller import AccessDBController

import threading


if __name__ == '__main__':
    application = QApplication(sys.argv)

    # controller = CRUDFileController()

    main_window = QMainWindow()
    window = Ui_MainWindow(main_window)

    access_db_view = AccessDBView(window)

    access_db_controller = AccessDBController(access_db_view)

    access_db_controller.get_access_db_view().get_window_ui().get_main_window().showMaximized()

    #
    # view = CRUDFileView(window)
    #
    # controller = CRUDFileController(view)
    #

    #file_event_handler = CRUDFileEventHandler(controller)

    #
    # controller.get_crud_file_view().get_main_window_ui().get_main_window().show()


    sys.exit(application.exec_())
