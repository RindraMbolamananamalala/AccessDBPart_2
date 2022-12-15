# -*- coding: utf-8 -*-

"""
accessdb_pii_hmi.py: The python file dedicated to the abstract definition of the HMI Superclass of the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from abc import ABC, abstractmethod


class AccessDBPIIHMI(ABC):
    @abstractmethod
    def show_hmi(self):
        """
        Displaying the main Element of the HMI
        :return:
        """
        # Just pass, letting the child classes manage it
        pass

    @abstractmethod
    def close_hmi(self):
        """
        Closing the main Element of the HMI
        :return:
        """
        # Just pass, letting the child classes manage it
        pass

    def __init__(self):
        # Just pass, letting the child classes manage it
        pass
