# -*- coding: utf-8 -*-

"""
access_db_dao_intf.py: The python file dedicated to the Abstract Base Class of the Data Access Object (DAO)
for any need of CRUD to Excel Files by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from abc import ABC, abstractmethod

from datetime import datetime

from BUSINESS.MODEL.DOMAIN_OBJECT.line_to_write_do import LineToWriteDO


class AccessDBDAOIntf(ABC):

    @abstractmethod
    def get_lines(self, file_path: str) -> list:
        """

        :param file_path: the Path of the Excel file
        :return: The filtered lines within the Excel file
        """
        return

    @abstractmethod
    def write_line(self, line: LineToWriteDO) -> datetime:
        """
        Saving in DB a line of information treated and returning the Current DateTime as a proof of the success of
        the operation (it will be useful at the level of the BUSINESS layer).

        :param line: The line to be saved
        :return: the Current DateTime as a proof of the success of the operation
        """
        return
