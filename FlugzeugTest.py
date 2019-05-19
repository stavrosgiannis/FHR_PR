from Flugzeug import Flugzeug

class FlugzeugTest():

    @staticmethod
    def test():
        testsequenz = [("FG3057P", 301), ("FG3295P", -1), ("F3290P", 56), ("FG4090S", 17), ("FG3200R", 114),
                       (None, 295)]

        for testfall in testsequenz:
            flugzeug = Flugzeug(testfall[0], testfall[1])

            print(flugzeug.getFlugzeugnummer() + "  =>  " + str(flugzeug.istFlugzeugGueltig()))


FlugzeugTest.test()
