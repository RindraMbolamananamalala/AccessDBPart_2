# -*- coding: utf-8 -*-

"""
line_to_read_do.py: The python file dedicated to the "Model:LineToReadDO" part of the MVC pattern implemented within
the "BUSINESS" layer of the Project, and at the same time one of the Project's DOs
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from BUSINESS.MODEL.DOMAIN_OBJECT.access_db_do import AccessDBDO


class LineToReadDO(AccessDBDO):

    def set_project(self, project: str):
        self.project = project

    def get_project(self) -> str:
        return self.project

    def set_family(self, family: str):
        self.family = family

    def get_family(self) -> str:
        return self.family

    def set_side_type(self, side_type: str):
        self.side_type = side_type

    def get_side_type(self) -> str:
        return self.side_type

    def set_sub(self, sub: str):
        self.sub = sub

    def get_sub(self) -> str:
        return self.sub

    def set_line_zone(self, line_zone: str):
        self.line_zone = line_zone

    def get_line_zone(self) -> str:
        return self.line_zone

    def set_type_of_material(self, type_of_material: str):
        self.type_of_material = type_of_material

    def get_type_of_material(self) -> str:
        return self.type_of_material

    def set_name(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_material_dpn(self, material_dpn: str):
        self.material_dpn = material_dpn

    def get_material_dpn(self) -> str:
        return self.material_dpn

    def set_material_dpn(self, material_dpn: str):
        self.material_dpn = material_dpn

    def get_material_dpn(self) -> str:
        return self.material_dpn

    def set_material_l_code(self, material_l_code: str):
        self.material_l_code = material_l_code

    def get_material_l_code(self) -> str:
        return self.material_l_code

    def set_box_type(self, box_type: str):
        self.box_type = box_type

    def get_box_type(self) -> str:
        return self.box_type

    def set_rack(self, rack: str):
        self.rack = rack

    def get_rack(self) -> str:
        return self.rack

    def set_level(self, level: str):
        self.level = level

    def get_level(self) -> str:
        return self.level

    def set_change_comment(self, change_comment: str):
        self.change_comment = change_comment

    def get_change_comment(self) -> str:
        return self.change_comment

    def set_cells(self, cells: str):
        self.cells = cells

    def get_cells(self) -> str:
        return self.cells
