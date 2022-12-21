# -*- coding: utf-8 -*-

"""
accessdb_pii_message_box.py: The python file dedicated to the implementation of the specific "Message Box" of
the Project.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

import ctypes


def message_box(title, text, style):
    """
    Defining the Message Box
    :param title: The title of the Message Box
    :param text: The text to be shown within the Message Box
    :param style: The preferred style for the Message Box (1 if a "Cancel" button is needed, 0 Otherwise)
    :return: The Message Box with all the preferences specified respected
    """
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


class AccessDBPIIMessageBox:

    def __init__(self, text: str):
        """

        :param text: The text to be shown within the Message Box
        """
        message_box('Information', text, 0)
