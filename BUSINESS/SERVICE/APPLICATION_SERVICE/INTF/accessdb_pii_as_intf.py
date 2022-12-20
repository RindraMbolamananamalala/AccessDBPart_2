# -*- coding: utf-8 -*-

"""
accessdb_pii_as_intf.py: The python file dedicated to the abstract class of the Application Service
part dedicated to any need of General service by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from abc import ABC, abstractmethod

from BUSINESS.MODEL.DOMAIN_OBJECT.line_weights_do import LineWeightsDO

class AccessDBPIIASIntf(ABC):

    @abstractmethod
    def read_mfg_data(self, zone_parameter: str, area_parameter: str) -> list:
        """
        Retrieving all the data contained in the MFG table corresponding to the parameters provided.
        :param zone_parameter: The "Zone" parameter
        :param area_parameter: The "Area" parameter
        :return: The list of all the MFG Lines corresponding to the parameters provided
        """
        pass

    @abstractmethod
    def save_line_weights(self, line_weights: LineWeightsDO):
        """
        Saving in DB the Line Weights DO specified as a parameter
        :param line_weights: The Line Weights DO to be saved
        :return: None
        """
        pass

    @abstractmethod
    def update_mfg_line_status(self, id: int):
        """
        Updating the Status of a MFG Line represented by its "id" (setting it to read)
        :param id: The id of the MFG Line to be updated
        :return: None
        """
        pass
