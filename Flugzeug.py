class Flugzeug():
    # ---------------------------------- a) --------------------------------------------------------
    def __init__(self, flugzeugnummer, maximalePassagieranzahl):
        self.__testnummer = 0

        if maximalePassagieranzahl < 0:
            maximalePassagieranzahl = 0

        self.__maximalePassagieranzahl = maximalePassagieranzahl

        if flugzeugnummer == None:
            self.__flugzeugnummer = "FG" + str(maximalePassagieranzahl + 3000) + "P"
        else:
            self.__flugzeugnummer = flugzeugnummer

    def getFlugzeugnummer(self):
        return self.__flugzeugnummer

    # --------------------------------------- b)---------------------------------------------------
    def istFlugzeugGueltig(self):

        if len(self.__flugzeugnummer) < 7 or len(self.__flugzeugnummer) > 8:
            return False

        if self.__flugzeugnummer[:2] != "FG":
            return False

        if self.__flugzeugnummer[-2:] == "TP":
            pZahl = self.__flugzeugnummer[2:-2]
            if pZahl >= 3000 and pZahl <= 3005:
                return True

        elif self.__flugzeugnummer[-1:0] == "P":
           