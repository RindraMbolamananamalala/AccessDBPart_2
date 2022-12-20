# -*- coding: utf-8 -*-

"""
line_weights.py: The python file dedicated to the "Model:Entity:LineWeights"  implemented within
the "BUSINESS" layer of the Project, and at the same time one of the Project's Entity
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from sqlalchemy import Column, Integer, String, DateTime, DECIMAL

from CONFIGURATIONS.application_properties import get_application_property

from DATA_ACCESS.data_access_base import Data_Access_Base

from BUSINESS.MODEL.ENTITY.accessdb_pii_entity import AccessDBPIIEntity


class LineWeights(Data_Access_Base, AccessDBPIIEntity):
    __tablename__ = get_application_property("db_line_weights_table_name")
    id = Column(Integer, primary_key=True, autoincrement=True)
    date_time = Column(DateTime)
    area = Column(String)
    aluminium = Column(DECIMAL(10, 2))
    copper = Column(DECIMAL(10, 2))
    plastic = Column(DECIMAL(10, 2))
    terminal = Column(DECIMAL(10, 2))
    harness = Column(DECIMAL(10, 2))
    team = Column(Integer)
    calendar_week = Column(DECIMAL(3, 1))
