# -*- coding: utf-8 -*-

"""
line_mfg.py: The python file dedicated to the "Model:Entity:LineMFG"  implemented within
the "BUSINESS" layer of the Project, and at the same time one of the Project's Entity
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from sqlalchemy import Column, Integer, String, DateTime, DECIMAL

from CONFIGURATIONS.application_properties import get_application_property

from BUSINESS.MODEL.ENTITY.accessdb_pii_entity import AccessDBPIIEntity

from DATA_ACCESS.data_access_base import Data_Access_Base


class LineMFG(Data_Access_Base, AccessDBPIIEntity):
    __tablename__ = get_application_property("db_line_to_write_table_name")
    id = Column(Integer, primary_key=True, autoincrement=True)
    date_time = Column(DateTime)
    area = Column(String)
    station = Column(String)
    item = Column(String)
    defect = Column(String)
    quantity = Column(Integer)
    material = Column(String)
    team = Column(Integer)
    calendar_week = Column(DECIMAL(3, 1))
    zone = Column(String)
