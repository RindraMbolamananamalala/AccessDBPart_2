# -*- coding: utf-8 -*-

"""
stanica_do.py: The python file dedicated to the "Model:StanicaDO" part of the MVC pattern implemented within
the "BUSINESS" layer of the Project, and at the same time one of the Project's DOs
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from BUSINESS.MODEL.DOMAIN_OBJECT.access_db_do import AccessDBDO


class StanicaDO(AccessDBDO):

    def set_label(self, label: str):
        self.label = label

    def get_label(self) -> str:
        return self.label

    def set_predmets(self, predmets: list):
        self.predmets = predmets

    def get_predmets(self) -> list:
        return self.predmets

    def __init__(self, *args):
        """

        :param stanica_label: The label of the Stanica.
        """
        if len(args) == 1:
            # The Stanica's Label was provided
            self.set_label(args[0])
            # Initializing the List of Predmets
            self.set_predmets([])

