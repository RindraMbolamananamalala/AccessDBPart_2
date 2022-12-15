
from datetime import datetime

from CONFIGURATIONS.logger import LOGGER
from CONFIGURATIONS.application_properties import get_application_property


from BUSINESS.MODEL.ENTITY.line_to_write import LineToWrite

from DATA_ACCESS.data_access_base import Session

from DATA_ACCESS.DAO.INTF.accessdb_pii_dao_intf import AccessDBPIIDAOIntf


class AccessDBPIIDAOImpl(AccessDBPIIDAOIntf):
    def get_mfg_lines(self, filter_parameter: str) -> list:
        """
        This function will return the list of MFG Lines when taking into account, with an "Area" filter, a
        "Time" filter: [06:00 - 14:00], []
        :param filter_parameter: The parameter to be used for the filtering of the MFG's lines to be read
        :return: The Entity list of MFG's lines filtered
        """
        try:
            # First, let's get the current time
            current_time = str(datetime.today().hour) + ":" + str(datetime.today().minute)
            print(current_time)
            with Session() as session:
                results = session.query(LineToWrite).filter_by(area=filter_parameter).all()
            if results:
                # At list one Line of MFG data has been retrieved
                return results
            # No Line of MFG data has been retrieved, therefore, let's return an empty list
            LOGGER.info("No MFG line corresponding to \"" + filter_parameter + "\"" + " has been found.")
            return []
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Retrieval Process. "
            )
            raise


