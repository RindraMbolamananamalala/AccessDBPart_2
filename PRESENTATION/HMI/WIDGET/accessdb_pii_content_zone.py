# -*- coding: utf-8 -*-

"""
access_db_pii_content_zone.py: The python file dedicated to the implementation of the "Zone" Content,
child of the abstract class "AccessDBPIIContentUI".
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PRESENTATION.HMI.WIDGET.accessdb_pii_content_ui import AccessDBPIIContentUI

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from CONFIGURATIONS.application_properties import get_application_property
from CONFIGURATIONS.logger import LOGGER


class AccessDBPIIContentZone(AccessDBPIIContentUI):

    def set_content_zone_options(self, content_zone_options: list):
        """

        :param content_zone_options: The list of options' buttons for the Content Zone
        :return:
        """
        self.content_zone_options = content_zone_options

    def get_content_zone_options(self) -> list:
        """

        :return: The list of options' buttons for the Content Zone
        """
        return self.content_zone_options

    def __init__(self, parent: QWidget):
        """

        :param parent: The Widget that will play the role of "Parent" for the the Content
        """
        # Letting the superclass managing the instantiation when the Parent is provided
        super(AccessDBPIIContentZone, self).__init__(parent)

        # The current Label for the description will have as text "Zone"
        self.label_bottom_description.setText(get_application_property("zone_label"))

        try:
            # Managing the Zone's options buttons
            self.set_content_zone_options([])
            option_list = get_application_property("zone_options").split(",")
            i = 0
            j = 0
            button_width = 400
            button_height = 200
            buttons_space_x = 370
            buttons_space_y = 275
            for cpt in range(0, len(option_list)):
                button_option = QPushButton(self.get_widget_content())
                button_option.setGeometry(
                    QRect(
                        (i * button_width) + buttons_space_x
                        , (j * button_height) + buttons_space_y
                        , 350
                        , 175)
                )
                button_option.setStyleSheet(u"background-color: #adaeaf;\n"
                                            "color: #1c2632;\n"
                                            "border-radius: 10px;")
                font1 = QFont()
                font1.setPointSize(22)
                font1.setFamily(u"Century Gothic")
                font1.setBold(False)
                button_option.setFont(font1)
                button_option.setText(option_list[cpt])
                button_option.setCursor(Qt.PointingHandCursor)
                button_option.show()
                self.get_content_zone_options().append(button_option)
                if i < 3:
                    i += 1
                else:
                    i = 0
                    j += 1
        except Exception as exception:
            # At least one error has occurred, therefore, stop the instantiation process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                    + ". Can't go further with the Instantiation Process. "
                )
            raise

