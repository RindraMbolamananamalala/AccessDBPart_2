# -*- coding: utf-8 -*-

"""
application_properties.py: The python file dedicated to the particular process of retrieving
the current Profile & current Profile's properties of the Project
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

import os
import configparser


# Fetching the path to the "application.ini" file
application_ini_file_path = ""
for i in range(0, len(os.getcwd().split("\\AccessDBPart_2")) - 1):
    application_ini_file_path += os.getcwd().split("\\AccessDBPart_2")[i] + "\\AccessDBPart_2"
application_ini_file_path = application_ini_file_path \
                                + "\\application.ini"

# preparing the Configurations
config = configparser.RawConfigParser()
config.read(application_ini_file_path)

# retrieving the chosen Profile
profile = config["PROFILE"]["value"]


def get_application_property(property_key) -> str:
    """
    Getting an application's property from the latter's "property_key".

    :param property_key: The property key of the wanted property
    :return: The value of the wanted property
    """
    return config[profile][property_key]



