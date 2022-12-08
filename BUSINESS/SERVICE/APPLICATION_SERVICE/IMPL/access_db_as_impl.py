# -*- coding: utf-8 -*-

"""
access_db_as_impl.py: The python file dedicated to the implementation class of the Application Service
part dedicated to any need of service by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from datetime import datetime

from BUSINESS.MODEL.DOMAIN_OBJECT.line_to_write_do import LineToWriteDO
from CONFIGURATIONS.logger import LOGGER

from BUSINESS.SERVICE.APPLICATION_SERVICE.INTF.access_db_as_intf import AccessDBASIntf

from DATA_ACCESS.DAO.INTF.access_db_dao_intf import AccessDBDAOIntf
from DATA_ACCESS.DAO.IMPL.access_db_dao_impl import AccessDBDAOImpl


class AccessDBASImpl(AccessDBASIntf):

    def write_line(self, line: LineToWriteDO) -> datetime:
        """
        Saving in DB a line of information treated and returning the Current DateTime as a proof of the success of
        the operation (it will be useful at the level of the CONTROLLER layer).

        :param line: The line to be saved
        :return: the Current DateTime as a proof of the success of the operation
        """
        try:
            return self.get_access_db_dao().write_line(line)
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Writing Process. "
            )
            raise

    def set_access_db_dao(self, access_db_dao: AccessDBDAOIntf):
        self.access_db_dao = access_db_dao

    def get_access_db_dao(self) -> AccessDBDAOIntf:
        return self.access_db_dao

    def get_lines(self, file_path: str) -> list:
        """

        :param file_path: the Path of the Excel file
        :return: The filtered lines within the Excel file
        """
        try:
            return self.get_access_db_dao().get_lines(file_path)
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Reading Process. "
            )
            raise

    def __init__(self):
        # Initializing the DAO to be used by the current Application Service
        self.set_access_db_dao(AccessDBDAOImpl())
