# -*- coding: utf-8 -*-

"""
accessdb_pii_view.py: The python file dedicated to the abstract definition of the VIEW Superclass of the Application,
part of the implementation of the MVC pattern within the latter.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PRESENTATION.HMI.accessdb_pii_hmi import AccessDBPIIHMI


class AccessDBPIIView(object):
    def set_corresponding_hmi(self, corresponding_hmi: AccessDBPIIHMI):
        """

        :param corresponding_hmi: The HMI object corresponding to the current VIEW
        :return:
        """
        self.corresponding_hmi = corresponding_hmi

    def get_corresponding_hmi(self) -> AccessDBPIIHMI:
        """

        :return: The HMI object corresponding to the current VIEW
        """
        return self.corresponding_hmi


    def __init__(self):
        # Just pass, letting the child classes managing it
        pass
