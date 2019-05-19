from Flugzeug import Flugzeug
from FlugzeugManager import FlugzeugManager
from Passagierauslastung import Passagierauslastung


# Arbeitspaket D
class PassagierauslastungTest():

    @staticmethod
    def test():
        manager = FlugzeugManager.getReferenz()
        F1 = Flugzeug("FG3050P", 125)
        F2 = Flugzeug("FG3051P", 112)
        F3 = Flugzeug("FG3052P", 145)
        manager.addFlugzeug(F1)
        manager.addFlugzeug(F2)
        manager.addFlugzeug(F3)

        testsequenz = [(F1.getFlugzeugnummer(), [77, 98, 117, 103, 125]), (F2.getFlugzeugnummer(), [109, 63, 88, 91]),
                       (F3.getFlugzeugnummer(), [58, 123, 77, 128, 109])]

        passagierauslastung = Passagierauslastung()

        for sequenz in testsequenz:
            passagierauslastung.setPassagierlisteProFlugzeug(sequenz[0], sequenz[1])

        if passagierauslastung.getMinimaleAuslastungInProzent(F1.getFlugzeugnummer()) != 61.6:
            return False
        if passagierauslastung.getMinimaleAuslastungInProzent(F2.getFlugzeugnummer()) != 56.25:
            return False
        if passagierauslastung.getMinimaleAuslastungInProzent(F3.getFlugzeugnummer()) != 40.0:
            return False
        if passagierauslastung.getFlugzeugnummerMitNiedrigsterAuslastung() != F3.getFlugzeugnummer():
            return False

        return True


print(PassagierauslastungTest.test())
