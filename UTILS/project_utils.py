# -*- coding: utf-8 -*-

"""
project_utils.py: The python file dedicated to the implementation of any need of Project's information anywhere in the
same Project.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

import os

project_name = "AccessDBPart_2"


def get_project_path() -> str:
    """

    :return: The path leading to the ROOT folder of the Project
    """
    project_path = ""
    for i in range(0, len(os.getcwd().split("\\" + project_name)) - 1):
        project_path += os.getcwd().split("\\" + project_name)[i] + "\\" + project_name
    return project_path.replace("\\", "\\\\")
