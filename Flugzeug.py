class Flugzeug():

    def __init__(self, flugzeugnummer, maximalePassagieranzahl):
        if maximalePassagieranzahl < 0:
            maximalePassagieranzahl = 0

        self.__maximalePassagieranzahl = maximalePassagieranzahl

        if flugzeugnummer == None:
            nummer = maximalePassagieranzahl + 3000
            self.__flugzeugnummer = "FG" + str(nummer) + "P"
        else:
            self.__flugzeugnummer = flugzeugnummer

    def getFlugzeugnummer(self):
        return self.__flugzeugnummer

    def getMaximalePassagieranzahl(self):
        return self.__maximalePassagieranzahl

    def istFlugzeugGueltig(self):

        if len(self.__flugzeugnummer) < 7 or len(self.__flugzeugnummer) > 8:
            return False

        if self.__flugzeugnummer[:2] != "FG":
            return False

        if self.__flugzeugnummer[-2:] == "TP":  # alternativ: self.__flugzeugnummer[len(self.__flugzeugnummer)-2:]
            zahl = int(self.__flugzeugnummer[2:-2])

            if zahl >= 3000 and zahl <= 3005:
                return True

        elif self.__flugzeugnummer[-1:] == "P":
            zahl = int(self.__flugzeugnummer[2:-1])

            if zahl >= 3025 and zahl <= 3295:
                return True

        elif self.__flugzeugnummer[-1:] == "S":
            zahl = int(self.__flugzeugnummer[2:-1])

            if zahl == 4010 or zahl == 4090:
                return True

        elif self.__flugzeugnummer[-1:] == "T":
            zahl = int(self.__flugzeugnummer[2:-1])

            if zahl >= 3000 and zahl <= 9999:
                return True

        return False

