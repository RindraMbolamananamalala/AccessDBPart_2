# -*- coding: utf-8 -*-

"""
number_converter.py: The python file dedicated to any need of conversion related to Numbers.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from CONFIGURATIONS.logger import LOGGER


def decimal_string_to_int(decimal_string: str, separator_character: str) -> int:
    """
    Convert a Decimal number provided as a string value into its Integer version (removing all the decimal parts)
    :param decimal_string: The Decimal number provided as a string value
    :param separator_character: The character used to separate the Integer and Decimal parts of the number to be converted
    :return: The Integer version of the Decimal number provided as a string value
    """
    try:
        int_part = decimal_string.split(separator_character)[0]
        return int(int_part)
    # At least one error has occurred, therefore, stop the process
    except Exception as exception:
        LOGGER.error(
            exception.__class__.__name__ + ": " + str(exception)
            + ". Can't go further with the Conversion process. "
        )
        raise

