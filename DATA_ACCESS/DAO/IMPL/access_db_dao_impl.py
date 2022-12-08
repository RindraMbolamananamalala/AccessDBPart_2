# -*- coding: utf-8 -*-

"""
access_db_dao_impl.py: The python file dedicated to the Implementation Class of the Data Access Object (DAO)
for any need of CRUD to Excel Files by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

import decimal
import pandas as pd
from datetime import datetime

from CONFIGURATIONS.logger import LOGGER

from CONFIGURATIONS.application_properties import get_application_property

from BUSINESS.MODEL.DOMAIN_OBJECT.line_to_read_do import LineToReadDO
from BUSINESS.MODEL.DOMAIN_OBJECT.line_to_write_do import LineToWriteDO
from BUSINESS.MODEL.ENTITY.line_to_write import LineToWrite

from DATA_ACCESS.DAO.INTF.access_db_dao_intf import AccessDBDAOIntf

from DATA_ACCESS.data_access_base import Session


class AccessDBDAOImpl(AccessDBDAOIntf):

    def get_lines(self, file_path: str) -> list:
        """

        :param file_path: the Path of the Excel file
        :return: The filtered lines within the Excel file
        """
        try:
            lines_retrieved = []
            file_raw = pd.read_excel(file_path)

            # Filtering the lines in function of the Columns
            column_b_filter = get_application_property("zone")
            column_d_filter = get_application_property("parameter1")
            column_e_filter = get_application_property("parameter2")

            file_filtered = file_raw[
                # Column B
                (file_raw["Family"] == column_b_filter)
                # Column D
                & (file_raw["SUB"] == column_d_filter)
                # Column E
                & (file_raw["LINE / ZONE"] == column_e_filter)
                ]

            # Saving the lines filtered
            for i in range(0, len(file_filtered)):
                line_retrieved = LineToReadDO()
                line_retrieved.set_project(file_filtered.iloc[i][0])
                line_retrieved.set_family(file_filtered.iloc[i][1])
                line_retrieved.set_side_type(file_filtered.iloc[i][2])
                line_retrieved.set_sub(file_filtered.iloc[i][3])
                line_retrieved.set_line_zone(file_filtered.iloc[i][4])
                line_retrieved.set_type_of_material(file_filtered.iloc[i][5])
                line_retrieved.set_name(file_filtered.iloc[i][6])
                line_retrieved.set_material_dpn(file_filtered.iloc[i][7])
                line_retrieved.set_material_l_code(file_filtered.iloc[i][8])
                line_retrieved.set_box_type(file_filtered.iloc[i][9])
                line_retrieved.set_rack(file_filtered.iloc[i][10])
                line_retrieved.set_level(file_filtered.iloc[i][11])
                line_retrieved.set_change_comment(file_filtered.iloc[i][12])
                line_retrieved.set_cells(file_filtered.iloc[i][13])
                lines_retrieved.append(line_retrieved)
            return lines_retrieved
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Reading Process. "
            )
            raise

    def write_line(self, line: LineToWriteDO) -> datetime:
        """
        Saving in DB a line of information treated and returning the Current DateTime as a proof of the success of
        the operation (it will be useful at the level of the BUSINESS layer).

        :param line: The line to be saved
        :return: the Current DateTime as a proof of the success of the operation
        """
        try:
            line_to_write = LineToWrite()
            datetime_today = datetime.today()
            line_to_write.date_time = datetime_today
            line_to_write.area = line.get_area()
            line_to_write.station = line.get_station()
            line_to_write.item = line.get_item()
            line_to_write.defect = line.get_defect()
            line_to_write.quantity = line.get_quantity()
            line_to_write.material = line.get_material()
            line_to_write.team = line.get_team()
            line_to_write.calendar_week = decimal.Decimal(
                str(datetime.today().isocalendar()[1])
                + "."
                + str(datetime.today().isocalendar()[2])
            )
            line_to_write.zone = line.get_zone()
            with Session() as session:
                session.add(line_to_write)
                session.commit()
            # The Writing was a success... so let's return the Current DateTime...
            return datetime_today
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Writing Process. "
            )
            raise
