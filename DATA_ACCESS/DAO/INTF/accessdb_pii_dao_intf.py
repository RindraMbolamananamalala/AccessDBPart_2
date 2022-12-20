# -*- coding: utf-8 -*-

"""
accessdb_pii_dao_intf.py: The python file dedicated to the Abstract Base Class of the Data Access Object (DAO)
for any need of CRUD to Excel Files by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from abc import ABC, abstractmethod

from BUSINESS.MODEL.DOMAIN_OBJECT.line_weights_do import LineWeightsDO


class AccessDBPIIDAOIntf(ABC):

    @abstractmethod
    def get_mfg_lines(self, filter_parameter: str) -> list:
        """

        :param filter_parameter: The parameter to be used for the filtering of the MFG's lines to be read
        :return: The list of MFG's lines filtered
        """
        return

    @abstractmethod
    def save_weights_line(self, weights_line: LineWeightsDO):
        """
        Saving a Line of Weights into DB
        :param weights_line: The Line of Weights object to be saved
        :return:
        """
        pass

    @abstractmethod
    def update_mfg_line_status(self, id: int):
        """
        Setting the Status of a MFG Line represented by its "id" to 1 (read)
        :param id: The id of the MFG Line to be updated
        :return: None
        """
        pass

