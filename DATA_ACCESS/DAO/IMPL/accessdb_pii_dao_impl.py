from datetime import datetime

from sqlalchemy import and_, or_, extract

from CONFIGURATIONS.logger import LOGGER
from CONFIGURATIONS.application_properties import get_application_property

from BUSINESS.MODEL.DOMAIN_OBJECT.line_mfg_do import LineMFGDO
from BUSINESS.MODEL.ENTITY.line_mfg import LineMFG

from DATA_ACCESS.data_access_base import Session

from DATA_ACCESS.DAO.INTF.accessdb_pii_dao_intf import AccessDBPIIDAOIntf


class AccessDBPIIDAOImpl(AccessDBPIIDAOIntf):

    def get_mfg_lines(self, zone_parameter: str, area_parameter: str) -> list:
        """
        This function will return the list of MFG Lines when taking into account, a "Zone" and an "Area" filter, and a
        "Time" filter: [06:00 - 14:00[, [14:00 - 22:00[, [22:00 - 06:00[
        :param zone_parameter: The "Zone" parameter to be used for the filtering of the MFG's lines to be read
        :param area_parameter: The "Area" parameter to be used for the filtering of the MFG's lines to be read
        :return: The Entity list of MFG's lines filtered
        """
        try:
            # First, let's get the current Time Stamp
            current_hour = datetime.today().hour
            if 6 <= current_hour < 14:
                time_stamp_min = 6
                time_stamp_max = 14
            elif 14 <= current_hour < 22:
                time_stamp_min = 14
                time_stamp_max = 22
            elif current_hour >= 22 or current_hour < 6:
                time_stamp_min = 22
                time_stamp_max = 6
            else:
                # Should never end up here...
                msg_error = "Impossible to find a Time Stamp for Current Hour : \"" + str(datetime.today().time()) + "\""
                LOGGER.error(msg_error)
                raise Exception(msg_error)

            # Now, it's time to fetch the data with the different Filters
            with Session() as session:
                if not (time_stamp_min == 22):
                    # It's not the Night..
                    results = session.query(LineMFG).filter(
                        and_(
                            # Filtering by "Zone"
                            LineMFG.zone == zone_parameter,
                            # Filtering by "Area"
                            LineMFG.area == area_parameter,
                            # Filtering by "Time Stamp"
                            and_(
                                extract("hour", LineMFG.date_time) >= time_stamp_min,
                                extract("hour", LineMFG.date_time) < time_stamp_max
                            )
                        )
                    ).all()
                else:
                    # It's the Night...
                    results = session.query(LineMFG).filter(
                        and_(
                            # Filtering by "Zone"
                            LineMFG.zone == zone_parameter,
                            # Filtering by "Area"
                            LineMFG.area == area_parameter,
                            # Filtering by "Time Stamp"
                            or_(
                                extract("hour", LineMFG.date_time) >= time_stamp_min,
                                extract("hour", LineMFG.date_time) < time_stamp_max
                            )
                        )
                    ).all()
            if results:
                """
                At list one Line of MFG data has been retrieved
                """
                # Converting the results into LineMFGDO
                lines_mfg_retrieved = []
                for result in results:
                    line_mfg = LineMFGDO()
                    line_mfg.set_date_time(result.date_time)
                    line_mfg.set_area(result.area)
                    line_mfg.set_station(result.station)
                    line_mfg.set_item(result.item)
                    line_mfg.set_defect(result.defect)
                    line_mfg.set_quantity(result.quantity)
                    line_mfg.set_material(result.material)
                    line_mfg.set_team(result.team)
                    line_mfg.set_calendar_week(result.calendar_week)
                    line_mfg.set_zone(result.zone)
                    lines_mfg_retrieved.append(line_mfg)
                return lines_mfg_retrieved
            # No Line of MFG data has been retrieved, therefore, let's return an empty list
            LOGGER.info(
                "No MFG line corresponding to parameters zone : \"" + zone_parameter
                + "\" and area : \"" + area_parameter + "\"" + " has been found"
                + " between " + str(time_stamp_min) + ":00 and " + str(time_stamp_max - 1) + ":59."
            )
            return []
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Retrieval Process. "
            )
            raise
