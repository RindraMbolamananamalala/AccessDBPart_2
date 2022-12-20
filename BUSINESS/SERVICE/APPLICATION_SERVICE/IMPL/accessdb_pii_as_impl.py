# -*- coding: utf-8 -*-

"""
accessdb_pii_as_mpl.py: The python file dedicated to the implementation class of the Application Service
part dedicated to any need of General service by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from BUSINESS.MODEL.DOMAIN_OBJECT.line_weights_do import LineWeightsDO
from BUSINESS.SERVICE.APPLICATION_SERVICE.INTF.accessdb_pii_as_intf import AccessDBPIIASIntf

from CONFIGURATIONS.logger import LOGGER

from DATA_ACCESS.DAO.INTF.accessdb_pii_dao_intf import AccessDBPIIDAOIntf
from DATA_ACCESS.DAO.IMPL.accessdb_pii_dao_impl import AccessDBPIIDAOImpl


class AccessDBPIIASImpl(AccessDBPIIASIntf):

    def set_accessdb_pii_dao(self, accessdb_pii_dao: AccessDBPIIDAOIntf):
        """

        :param accessdb_pii_dao: The Access DB Part II general DAO to be used by the current AS
        :return:
        """
        self.accessdb_pii_dao = accessdb_pii_dao

    def get_accessdb_pii_dao(self):
        """

        :return: The Access DB Part II general DAO to used by the current AS
        """
        return self.accessdb_pii_dao

    def read_mfg_data(self, zone_parameter: str, area_parameter: str) -> list:
        """
        Retrieving all the data contained in the MFG table corresponding to the parameters provided.
        :param zone_parameter: The "Zone" parameter
        :param area_parameter: The "Area" parameter
        :return: The list of all the MFG Lines corresponding to the parameters provided
        """
        try:
            return self.get_accessdb_pii_dao().get_mfg_lines(zone_parameter, area_parameter)
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Retrieval Process. "
            )
            raise

    def save_line_weights(self, line_weights: LineWeightsDO):
        """
        Saving in DB the Line Weights DO specified as a parameter
        :param line_weights: The Line Weights DO to be saved
        :return: None
        """
        try:
            self.get_accessdb_pii_dao().save_weights_line(line_weights)
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Save Process. "
            )
            raise

    def __init__(self):
        # Initializing the DAO
        self.set_accessdb_pii_dao(AccessDBPIIDAOImpl())