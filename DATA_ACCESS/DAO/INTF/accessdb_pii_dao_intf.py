# -*- coding: utf-8 -*-

"""
accessdb_pii_dao_intf.py: The python file dedicated to the Abstract Base Class of the Data Access Object (DAO)
for any need of CRUD to Excel Files by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from abc import ABC, abstractmethod

from datetime import datetime


class AccessDBPIIDAOIntf(ABC):

    @abstractmethod
    def get_mfg_lines(self, filter_parameter: str) -> list:
        """

        :param filter_parameter: The parameter to be used for the filtering of the MFG's lines to be read
        :return: The list of MFG's lines filtered
        """
        return

