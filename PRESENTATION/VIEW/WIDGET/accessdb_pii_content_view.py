# -*- coding: utf-8 -*-

"""
accessdb_pii_content_view.py: The python file dedicated to the abstract definition of the VIEW:Content of
the Application, part of the implementation of the MVC pattern within the latter.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PRESENTATION.VIEW.accessdb_pii_view import AccessDBPIIView


class AccessDBPIIContentView(AccessDBPIIView):

    def __init__(self):
        # First, let's call the Superclass' __init__() function
        super(AccessDBPIIView, self).__init__()

    def manage_notification_by_parent(self):
        """
        The Parent View has sent a Notification, let's manage it in function of the current Child's type...
        """
        # ... but, just Pass for the moment, let the child manage it..
        pass



