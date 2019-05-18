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

    def addZuladung(self, Zuladung):
        if self.istZuladungZulaessig(Zuladung):
            self.__zuladungsliste.append(Zuladung)
            return True
        return False

    def istZuladungZulaessig(self, Zuladung):

        summeGewicht = 0

        for zuladungVorhanden in self.__zuladungsliste:
            stundeStart = zuladungVorhanden.start
            dauerZuladung = zuladungVorhanden.dauer
            gewicht = zuladungVorhanden.gewicht

            if (stundeStart <= Zuladung.start + Zuladung.dauer) and (Zuladung.start <= stundeStart + dauerZuladung):
                summeGewicht = summeGewicht + gewicht

        if summeGewicht + Zuladung.gewicht <= self.__maximalesZuladungsgewicht:
            return True
        else:
            return False
