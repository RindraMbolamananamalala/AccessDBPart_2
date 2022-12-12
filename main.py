import sys
import time

from PySide2.QtWidgets import *

from PRESENTATION.HMI.ui_AccessDB_PII_MainWindow_GUI import Ui_MainWindow
from PRESENTATION.HMI.WIDGET.accessdb_pii_content_zone import AccessDBPIIContentZone
from PRESENTATION.HMI.WIDGET.access_db_pii_content_body_zone import AccessDBPIIContentBodyZone
from PRESENTATION.HMI.WIDGET.accessdb_pii_content_familije import AccessDBPIIContentFamilije
from PRESENTATION.HMI.FORM.form_weigh_material_ui import FormWeighMaterialUI

if __name__ == '__main__':
    application = QApplication(sys.argv)

    main_window = QMainWindow()

    ui_main_window = Ui_MainWindow(main_window)
    ui_main_window.get_main_window().showMaximized()

    content_zone = AccessDBPIIContentZone(ui_main_window.get_widget_content())

    content_body_zone = AccessDBPIIContentBodyZone(ui_main_window.get_widget_content())

    content_familije = AccessDBPIIContentFamilije(ui_main_window.get_widget_content())

    form_weigh_material = FormWeighMaterialUI(None)
    form_weigh_material.get_form_weigh_material().show()

    ui_main_window.set_content(content_zone)



    # controller = CRUDFileController()

    """
    WORKED FOR PI (beginning)
    """
    # main_window = QMainWindow()
    # window = Ui_MainWindow(main_window)
    #
    # access_db_view = AccessDBView(window)
    #
    # access_db_controller = AccessDBController(access_db_view)
    #
    # access_db_controller.get_access_db_view().get_window_ui().get_main_window().showMaximized()

    """
    WORKED FOR PI (end)
    """

    #
    # view = CRUDFileView(window)
    #
    # controller = CRUDFileController(view)
    #

    # file_event_handler = CRUDFileEventHandler(controller)

    #
    # controller.get_crud_file_view().get_main_window_ui().get_main_window().show()

    sys.exit(application.exec_())
