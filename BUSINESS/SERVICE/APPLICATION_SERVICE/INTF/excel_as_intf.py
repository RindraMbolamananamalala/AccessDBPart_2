# -*- coding: utf-8 -*-

"""
excel_as_intf.py: The python file dedicated to the abstract class of the Application Service
part dedicated to any need of Excel service by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from abc import ABC, abstractmethod


class ExcelASIntf(ABC):

    @abstractmethod
    def create_submition_excel_file(self):
        """
        Creating the Excel file for the "Submition", naming it, storing it in the dedicated folder and then returning
        its whole file path.
        :return: The file path of the Excel file for the "Submition" newly-created.
        """
        pass

    @abstractmethod
    def insert_categorized_lines(self, team: str
                                        , area_parameter: str
                                        , category: str
                                        , categorized_lines: list
                                        , excel_file_submition_path: str):
        """
        Inserting all the information corresponding to the Categorized Lines within the Excel File for the "Submition".
        :param team: The "Team" parameter selected
        :param area_parameter: The "Area" parameter selected
        :param category: The Category (Material) concerned inside the Excel File
        :param categorized_lines: The categorize lines to be inserted
        :param excel_file_submition_path: The path leading to the Excel File for the Submition process
        :return:
        """
        pass

    @abstractmethod
    def print_excel_file(self, excel_file_path: str):
        """
        Printing an Excel file whose path has been specified as an argument with the current (default) printer of
        the Computer.
        :param excel_file_path: The path of the Excel File to be printed
        :return: None
        """
        pass
