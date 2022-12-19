# -*- coding: utf-8 -*-

"""
form_weight_material_view.py: The python file dedicated to the implementation of the VIEW:FormWeightMaterial of
the Application, part of the implementation of the MVC pattern within the latter.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from decimal import Decimal

from CONFIGURATIONS.logger import LOGGER

from PRESENTATION.HMI.FORM.form_weight_material_ui import FormWeightMaterialUI

from PRESENTATION.VIEW.accessdb_pii_view import AccessDBPIIView


class FormWeightMaterialView(AccessDBPIIView):

    def __init__(self, material: str):
        """

        :param material: The Material currently concerned by the Weight precision.
        """
        #  First, let's call the Superclass' __init__() function
        super(FormWeightMaterialView, self).__init__()

        # Then, let's assign an instance of Form Weight Material UI with the Material concerned  as the
        # GUI corresponding to the current view
        self.set_corresponding_hmi(FormWeightMaterialUI(None))
        self.get_corresponding_hmi().get_label_material().setText(material)

        # At the beginning, the "Button OK" is disabled and is waiting for a valid Weight text input by the User to
        # be enabled
        button_ok = self.get_corresponding_hmi().get_button_ok()
        button_ok.setEnabled(False)
        button_ok.setStyleSheet(u"border-radius: 25px;\n"
                                "background-color: gray;\n"
                                "color: #d2d2d2;")

        # Now, it's time to manage the Events
        self.manage_events()

    def manage_events(self):
        """
        Managing every events related to the View
        :return: None
        """
        # Management of the Availability of the "Button OK"
        self.get_corresponding_hmi().get_input_text_weight().textChanged.connect(self.enable_button_ok)

    def enable_button_ok(self):
        """
        Enabling the "Button OK" if all the requirements specified by the Management Rules have been satisfied,
        otherwise, always Disabling it.
        :return: None
        """
        try:
            button_ok = self.get_corresponding_hmi().get_button_ok()
            # Enabling the "Button OK" if the corresponding requirements are satisfied
            if self.are_conditions_to_enable_button_ok_satisfied():
                # conditions satisfied
                button_ok.setEnabled(True)
                button_ok.setStyleSheet(u"border-radius: 25px;\n"
                                        "background-color: #1c2632;\n"
                                        "color: #d2d2d2;")
            else:
                # conditions not satisfied
                button_ok.setEnabled(False)
                button_ok.setStyleSheet(u"border-radius: 25px;\n"
                                        "background-color: gray;\n"
                                        "color: #d2d2d2;")
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Button Management process. "
            )
            raise

    def are_conditions_to_enable_button_ok_satisfied(self):
        """
        1 - Text can't be Null
        2 - Text can't be 0,00
        3 - The number of decimals must be 2
        4 - Number of Integer greater than O
        :return: True if all the conditions have been satisfied, False otherwise.
        """
        input_text_weight = self.get_corresponding_hmi().get_input_text_weight()
        input_text_weight_text = input_text_weight.text()
        # 1 - Text can't be Null
        try:
            text_not_null = (len(input_text_weight_text) > 0)
        except:
            # An error has made the evaluation impossible, Directly false then
            text_not_null = False
        # 2 - Text can't be 0,00
        try:
            text_not_zero = (Decimal(input_text_weight_text.replace(",", ".")) > 0)
        except:
            # An error has made the evaluation impossible, Directly false then
            text_not_zero = False
        # 3 - The number of decimals must be 2
        try:
            number_of_decimals_is_2 = (len(input_text_weight_text.split(",")[1]) == 2)
        except:
            # An error has made the evaluation impossible, Directly false then
            number_of_decimals_is_2 = False
        # 4 - Number of Integer greater than O
        try:
            number_of_integer_greater_than_0 = (len(input_text_weight_text.split(",")[0]) > 0)
        except:
            # An error has made the evaluation impossible, Directly false then
            number_of_integer_greater_than_0 = False
        # Combining all the evaluations
        return text_not_null \
               & text_not_zero \
               & number_of_decimals_is_2 \
               & number_of_integer_greater_than_0

