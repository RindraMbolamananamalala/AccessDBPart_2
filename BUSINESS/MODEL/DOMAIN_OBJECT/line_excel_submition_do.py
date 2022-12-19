# -*- coding: utf-8 -*-

"""
line_excel_submition_do.py: The python file dedicated to the "Model:LineExcelSubmition" part of the MVC pattern
implemented within the "BUSINESS" layer of the Project, and at the same time one of the Project's DOs
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from BUSINESS.MODEL.DOMAIN_OBJECT.accessdb_pii_do import AccessDBPIIDO


class LineExcelSubmitionDO(AccessDBPIIDO):

    def set_category(self, category: str):
        self.category = category

    def get_category(self) -> str:
        return self.category

    def set_material_id(self, material_id: str):
        self.material_id = material_id

    def get_material_id(self) -> str:
        return self.material_id

    def set_quantity(self, quantity: int):
        self.quantity = quantity

    def get_quantity(self) -> int:
        return self.quantity

    def __init__(self):
        # Initializing all properties' values
        self.set_category(None)
        self.set_material_id(None)
        self.set_quantity(None)
