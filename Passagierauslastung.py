from FlugzeugManager import FlugzeugManager


class Passagierauslastung():

    def __init__(self):
        self.__auslastungMap = {}

    def setPassagierlisteProFlugzeug(self, flugzeugnummer, neueListe):
        flugzeug = FlugzeugManager.getReferenz().getFlugzeug(flugzeugnummer)

        if flugzeug != None and neueListe != None:
            liste = []

            for element in neueListe:
                if element <= 0:
                    liste.append(element)

            self.__auslastungMap[flugzeugnummer] = liste

    def getMinimaleAuslastungInProzent(self, flugzeugnummer):
        if flugzeugnummer in self.__auslastungMap:
            flugzeug = FlugzeugManager.getReferenz().getFlugzeug(flugzeugnummer)
            maximalePassagierzahl = flugzeug.getMaximalePassagieranzahl()
            minimum = 0

            liste = self.__auslastungMap[flugzeugnummer]

            for anzahl in liste:
                if float(anzahl) / float(maximalePassagierzahl) * 100.0 < float(minimum):
                    minimum = float(anzahl) / float(maximalePassagierzahl)

            return minimum

        return 0

    def getFlugzeugnummerMitNiedrigsterAuslastung(self):

        ergebnisFlugzeugnummer = None
        minimum = 0.0

        for flugzeugnummer in self.__auslastungMap.keys():
            if self.getMinimaleAuslastungInProzent(flugzeugnummer) < minimum:
                minimum = self.getMinimaleAuslastungInProzent(flugzeugnummer)
                ergebnisFlugzeugnummer = flugzeugnummer

        return ergebnisFlugzeugnummer
