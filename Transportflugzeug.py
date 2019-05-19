from Flugzeug import Flugzeug


class Transportflugzeug(Flugzeug):

    def __init__(self, flugzeugnummer, maximalePassagieranzahl, maximalesZuladungsgewicht):
        # Konstruktor der Vaterklasse aufrufen:
        super().__init__(flugzeugnummer, maximalePassagieranzahl)

        if maximalesZuladungsgewicht <= 0:
            maximalesZuladungsgewicht = 1000

        self.__maximalesZuladungsgewicht = maximalesZuladungsgewicht
        # Die Liste der Zuladungen:
        self.__zuladungsliste = []


    def getMaximalesZuladungsgewicht(self):
        return self.__maximalesZuladungsgewicht

    def addZuladung(self, zuladung):
        if self.istZuladungZulaessig(zuladung):
            self.__zuladungsliste.append(zuladung)
            return True

        return False

    def istZuladungZulaessig(self, zuladung):

        summeGewicht = 0

        for zuladungVorhanden in self.__zuladungsliste:
            stundeStart = zuladungVorhanden.start
            dauerZuladung = zuladungVorhanden.dauer
            gewicht = zuladungVorhanden.gewicht

            if (stundeStart <= zuladung.start + zuladung.dauer) and (zuladung.start <= stundeStart + dauerZuladung):
                summeGewicht = summeGewicht + gewicht

        if summeGewicht + zuladung.gewicht <= self.__maximalesZuladungsgewicht:
            return True
        else:
            return False
