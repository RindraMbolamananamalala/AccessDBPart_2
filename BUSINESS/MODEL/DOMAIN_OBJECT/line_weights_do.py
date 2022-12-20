# -*- coding: utf-8 -*-

"""
line_weights_do.py: The python file dedicated to the "Model:LineWeightsDO" part of the MVC pattern
implemented within the "BUSINESS" layer of the Project, and at the same time one of the Project's DOs
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

import datetime

import decimal

from BUSINESS.MODEL.DOMAIN_OBJECT.accessdb_pii_do import AccessDBPIIDO


class LineWeightsDO(AccessDBPIIDO):

    def set_date_time(self, date_time: datetime.datetime):
        self.date_time = date_time

    def get_date_time(self) -> datetime.datetime:
        return self.date_time

    def set_area(self, area: str):
        self.area = area

    def get_area(self) -> str:
        return self.area

    def set_aluminium_weight(self, aluminium_weight: decimal.Decimal):
        self.aluminium_weight = aluminium_weight

    def get_aluminium_weight(self) -> decimal.Decimal:
        return self.aluminium_weight

    def set_copper_weight(self, copper_weight: decimal.Decimal):
        self.copper_weight = copper_weight

    def get_copper_weight(self) -> decimal.Decimal:
        return self.copper_weight

    def set_plastic_weight(self, plastic_weight: decimal.Decimal):
        self.plastic_weight = plastic_weight

    def get_plastic_weight(self) -> decimal.Decimal:
        return self.plastic_weight

    def set_terminal_weight(self, terminal_weight: decimal.Decimal):
        self.terminal_weight = terminal_weight

    def get_terminal_weight(self) -> decimal.Decimal:
        return self.terminal_weight

    def set_harness_weight(self, harness_weight: decimal.Decimal):
        self.harness_weight = harness_weight

    def get_harness_weight(self) -> decimal.Decimal:
        return self.harness_weight

    def set_team(self, team: int):
        self.team = team

    def get_team(self) -> int:
        return self.team

    def set_calendar_week(self, calendar_week: decimal.Decimal):
        self.calendar_week = calendar_week

    def get_calendar_week(self) -> decimal.Decimal:
        return self.calendar_week

    def __init__(self):
        # Initializing all the Properties to None
        self.set_date_time(None)
        self.set_area(None)
        self.set_aluminium_weight(None)
        self.set_copper_weight(None)
        self.set_plastic_weight(None)
        self.set_terminal_weight(None)
        self.set_harness_weight(None)
        self.set_team(None)
        self.set_calendar_week(None)