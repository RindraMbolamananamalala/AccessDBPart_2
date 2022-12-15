
class AccessDBPIIEntity():

    def __str__(self) -> str:
        """

        :return:  a structure in which all Entity's attributes are presented besides their respective value(s)
        """
        return super.__str__(self) + " :" + str(vars(self))
