# -*- coding: utf-8 -*-

"""
accessdb_pii_content_body_zone_view.py: The python file dedicated to the implementation of the VIEW:ContentBodyZone of
the Application, part of the implementation of the MVC pattern within the latter.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PySide2.QtWidgets import *

from PRESENTATION.HMI.WIDGET.access_db_pii_content_body_zone import AccessDBPIIContentBodyZone

from PRESENTATION.VIEW.WIDGET.accessdb_pii_content_view import AccessDBPIIContentView


class AccessDBPIIContentBodyZoneView(AccessDBPIIContentView):

    def __init__(self, parent: QWidget):
        #  First, let's call the Superclass' __init__() function
        super(AccessDBPIIContentBodyZoneView, self).__init__()

        # and then, let's associate the View with an AccessDB Part II's Body Zone content UI
        self.set_corresponding_hmi(AccessDBPIIContentBodyZone(parent))