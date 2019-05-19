from Transportflugzeug import Transportflugzeug
from Zuladung import Zuladung


# Arbeitspaket B e)
class TransportflugzeugTest():

    @staticmethod
    def test():
        zuladungssequenz = [(1, 3, 510), (2, 2, 6510), (2, 4, 510), (5, 8, 3000), (4, 7, 2500), (6, 1, 1010),
                            (5, 3, 510)]

        transportflugzeug = Transportflugzeug("FG3001TP", 3, 5000)

        for zuladungswerte in zuladungssequenz:
            zuladung = Zuladung(zuladungswerte[0], zuladungswerte[1], zuladungswerte[2])

            istZulaessig = transportflugzeug.addZuladung(zuladung)
            print(transportflugzeug.getFlugzeugnummer() + " (" + str(zuladung.start) + ", " + str(
                zuladung.dauer) + ", " + str(zuladung.gewicht) + ") => " + str(istZulaessig))


TransportflugzeugTest.test()
