# -*- coding: utf-8 -*-

"""
excel_as_impl.py: The python file dedicated to the implementation class of the Application Service
part dedicated to any need of Excel service by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

import os
import shutil
import uuid

from datetime import datetime

from UTILS.project_utils import get_project_path

from CONFIGURATIONS.logger import LOGGER
from CONFIGURATIONS.application_properties import get_application_property

from BUSINESS.SERVICE.APPLICATION_SERVICE.INTF.excel_as_intf import ExcelASIntf


def generate_name_for_submition_excel_file(zone_parameter: str) -> str:
    """
    Generating a name for the Excel File for the Submition, while respecting the indications of the Management Rules
    about this name.
    :param zone_parameter: The "Zone" parameter to be included within the file's name
    :return: The name formulated according to the Management Rules corresponding to it
    """
    try:
        date = datetime.today().date()
        time = str(datetime.today().time()).replace(".", ",")  # In order to see the decimals
        unique_id = uuid.uuid4()
        name_generated = str(date) + "_" + str(time) + "_" + zone_parameter + "_" + str(unique_id)
        # making it possible to distinguish the time but at the same time respecting the rules for the name of
        # an Excel file
        return name_generated.replace(":", ".")
    except Exception as exception:
        # At least one error has occurred, therefore, stop the process
        LOGGER.error(
            exception.__class__.__name__ + ": " + str(exception)
            + ". Can't go further with the file name Generation Process. "
        )
        raise


class ExcelASImpl(ExcelASIntf):

    def create_submition_excel_file(self, zone_parameter: str) -> str:
        """
        Creating the Excel file for the "Submition", naming it, storing it in the dedicated folder and then returning
        its whole file path.
        :return: The file path of the Excel file for the "Submition" newly-created.
        """
        try:
            # STEP 1 : Let's have an empty copy of the Submition Excel file template within the folder dedicated to the
            # Excel Files for the actual Submition processes, and name it with the name specifically generated for it
            project_path = get_project_path()
            template_path = project_path + "\\RESOURCES\\EXCEL\\scrap_submition_template.xlsx"
            excel_submition_path = get_application_property("excel_created_folder_path") \
                                   + "\\" \
                                   + generate_name_for_submition_excel_file(zone_parameter) + ".xlsx"
            shutil.copyfile(template_path, excel_submition_path)
            # Excel File for Submition successfully created
            LOGGER.info("The Excel file for the Submition: \"" + excel_submition_path + "\" is successfully created")
            # STEP 2: Returning the whole file Path
            return excel_submition_path
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the file Creation Process. "
            )
            raise


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
