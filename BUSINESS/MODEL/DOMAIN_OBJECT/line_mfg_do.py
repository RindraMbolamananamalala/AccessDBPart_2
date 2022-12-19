# -*- coding: utf-8 -*-

"""
line_mfg_do.py: The python file dedicated to the "Model:LineMFGDO" part of the MVC pattern implemented within
the "BUSINESS" layer of the Project, and at the same time one of the Project's DOs
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

import datetime

import decimal

from BUSINESS.MODEL.DOMAIN_OBJECT.accessdb_pii_do import AccessDBPIIDO


class LineMFGDO(AccessDBPIIDO):
    def set_date_time(self, date_time: datetime.datetime):
        self.date_time = date_time

    def get_date_time(self) -> datetime.datetime:
        return self.date_time

    def set_area(self, area: str):
        self.area = area

    def get_area(self) -> str:
        return self.area

    def set_station(self, station: str):
        self.station = station

    def get_station(self) -> str:
        return self.station

    def set_item(self, item: str):
        self.item = item

    def get_item(self) -> str:
        return self.item

    def set_defect(self, defect: str):
        self.defect = defect

    def get_defect(self) -> str:
        return self.defect

    def set_quantity(self, quantity: int):
        self.quantity = quantity

    def get_quantity(self) -> int:
        return self.quantity

    def set_material(self, material: str):
        self.material = material

    def get_material(self) -> str:
        return self.material

    def set_team(self, team: int):
        self.team = team

    def get_team(self) -> int:
        return self.team

    def set_calendar_week(self, calendar_week: decimal.Decimal):
        self.calendar_week = calendar_week

    def get_calendar_week(self) -> decimal.Decimal:
        return self.calendar_week

    def set_zone(self, zone: str):
        self.zone = zone

    def get_zone(self) -> str:
        return self.zone
