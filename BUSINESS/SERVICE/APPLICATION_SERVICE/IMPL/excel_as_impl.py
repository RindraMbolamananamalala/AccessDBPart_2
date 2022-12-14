# -*- coding: utf-8 -*-

"""
excel_as_impl.py: The python file dedicated to the implementation class of the Application Service
part dedicated to any need of Excel service by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

import os

from CONFIGURATIONS.logger import LOGGER

from BUSINESS.SERVICE.APPLICATION_SERVICE.INTF.excel_as_intf import ExcelASIntf


class ExcelASImpl(ExcelASIntf):

    def print_excel_file(self, excel_file_path: str):
        """
        Printing an Excel file whose path has been specified as an argument with the current (default) printer of
        the Computer.
        :param excel_file_path: The path of the Excel File to be printed
        :return: None
        """
        try:
            os.startfile(excel_file_path, 'print')
            # The Excel file has been successfully printed
            success_msg = "The Excel file : \"" + excel_file_path + "\"" + "has been successfully printed."
            LOGGER.info(success_msg)
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Printing Process. "
            )
            raise
