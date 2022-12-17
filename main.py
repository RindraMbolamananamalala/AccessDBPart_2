import sys
import time

from PySide2.QtWidgets import *


from PRESENTATION.HMI.WIDGET.accessdb_pii_content_zone import AccessDBPIIContentZone
from PRESENTATION.HMI.WIDGET.access_db_pii_content_body_zone import AccessDBPIIContentBodyZone
from PRESENTATION.HMI.WIDGET.accessdb_pii_content_familije import AccessDBPIIContentFamilije
from PRESENTATION.HMI.FORM.form_weight_material_ui import FormWeightMaterialUI
from PRESENTATION.HMI.FORM.form_weights_validation_ui import FormWeightsValidationUI

from PRESENTATION.VIEW.FORM.form_weight_material_view import FormWeightMaterialView

from PRESENTATION.CONTROLLER.accessdb_pii_controller import AccessDBPIIController

if __name__ == '__main__':
    application = QApplication(sys.argv)

    # main_window = QMainWindow()
    #
    # ui_main_window = Ui_MainWindow(main_window)
    # ui_main_window.get_main_window().showMaximized()
    #
    # content_zone = AccessDBPIIContentZone(ui_main_window.get_widget_content())
    #
    # content_body_zone = AccessDBPIIContentBodyZone(ui_main_window.get_widget_content())
    #
    # content_familije = AccessDBPIIContentFamilije(ui_main_window.get_widget_content())
    #
    # form_weigh_material = FormWeighMaterialUI(None)
    # form_weighs_validation = FormWeighsValidationUI(None)
    #
    # form_weighs_validation.get_form_weighs_validation().show()
    #
    # ui_main_window.set_content(content_zone)

    """
    PRE VALIDATION
    """
    # controller = AccessDBPIIController()

   # controller.get_accessdb_pii_main_window_view().get_corresponding_hmi().get_main_window().showMaximized()
    """
    PRE VALIDATION
    """

    form_weight_view = FormWeightMaterialView()

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
