# -*- coding: utf-8 -*-

"""
accessdb_pii_content_familijie_view.py: The python file dedicated to the implementation of the VIEW:ContentFamilijie of
the Application, part of the implementation of the MVC pattern within the latter.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PySide2.QtWidgets import *

from PRESENTATION.HMI.WIDGET.accessdb_pii_content_familije import AccessDBPIIContentFamilije

from PRESENTATION.VIEW.WIDGET.accessdb_pii_content_view import AccessDBPIIContentView


class AccessDBPIIContentFamilijeView(AccessDBPIIContentView):

    def __init__(self, parent: QWidget):
        #  First, let's call the Superclass' __init__() function
        super(AccessDBPIIContentFamilijeView, self).__init__()

        # and then, let's associate the View with an AccessDB Part II's Familije content UI
        self.set_corresponding_hmi(AccessDBPIIContentFamilije(parent))
