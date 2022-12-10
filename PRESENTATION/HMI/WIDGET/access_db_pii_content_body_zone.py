# -*- coding: utf-8 -*-

"""
access_db_pii_content_body_zone.py: The python file dedicated to the implementation of the "Body Zone" Content,
child of the abstract class "AccessDBPIIContentUI".
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"


from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from CONFIGURATIONS.application_properties import get_application_property
from CONFIGURATIONS.logger import LOGGER

from PRESENTATION.HMI.WIDGET.accessdb_pii_content_ui import AccessDBPIIContentUI


class AccessDBPIIContentBodyZone(AccessDBPIIContentUI):

    def __init__(self, parent: QWidget):
        """

        :param parent: The Widget that will play the role of "Parent" for the the Content
        """
        try:
            # Letting the superclass managing the instantiation when the Parent is provided
            super(AccessDBPIIContentBodyZone, self).__init__(parent)

            # The current Label for the description will have as text "Body zone"
            self.label_bottom_description.setText("Body zone")

            # Loading the Body Zone's options buttons
            option_list = get_application_property("body_zone_options").split(",")
            i = 0
            j = 0
            button_width = 400
            button_height = 200
            buttons_space_x = 170
            buttons_space_y = 75
            for cpt in range(0, len(option_list)):
                button_option = QPushButton(self.get_widget_content())
                button_option .setGeometry(
                    QRect(
                        (i * button_width) + buttons_space_x
                        , (j * button_height) + buttons_space_y
                        , 350
                        , 175)
                )
                button_option .setStyleSheet(u"background-color: #adaeaf;\n"
                                              "color: #1c2632;\n"
                                              "border-radius: 10px;")
                font1 = QFont()
                font1.setPointSize(22)
                font1.setFamily(u"Century Gothic")
                font1.setBold(False)
                button_option.setFont(font1)
                button_option.setText(option_list[cpt])
                button_option.show()
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






