# -*- coding: utf-8 -*-

"""
access_db_as_intf.py: The python file dedicated to the Abstract Base Class of the Application Service
part dedicated to any need of service by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from abc import ABC, abstractmethod

from datetime import datetime

from BUSINESS.MODEL.DOMAIN_OBJECT.line_to_write_do import LineToWriteDO

class AccessDBASIntf(ABC):

    @abstractmethod
    def get_lines(self, file_path: str):
        """

        :param file_path: the Path of the Excel file
        :return: The filtered lines within the Excel file
        """
        return

    @abstractmethod
    def write_line(self, line: LineToWriteDO) -> datetime:
        """
        Saving in DB a line of information treated and returning the Current DateTime as a proof of the success of
        the operation (it will be useful at the level of the CONTROLLER layer).

        :param line: The line to be saved
        :return: the Current DateTime as a proof of the success of the operation
        """
        return
