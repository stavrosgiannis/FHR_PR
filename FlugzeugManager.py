class FlugzeugManager():
    # Arbeitspaket c a und b)
    __referenz = None

    def __init__(self):
        self.__passagierflugzeugMap = {}
        self.__transportflugzeugMap = {}
        self.__sonstigeFlugzeugMap = {}

    @staticmethod
    def getReferenz():
        if FlugzeugManager.__referenz is None:
            FlugzeugManager.__referenz = FlugzeugManager()
        return FlugzeugManager.__referenz

    # Arbeitspaket c c)
    def addFlugzeug(self, flugzeug):
        if flugzeug is None or not flugzeug.istFlugzeugGueltig():
            return False

        flugzeugnummer = flugzeug.getFlugzeugnummer()

        if flugzeugnummer[-2:] == "TP":
            self.__transportflugzeugMap[flugzeugnummer] = flugzeug
        elif flugzeugnummer[-1:] == "P":
            self.__passagierflugzeugMap[flugzeugnummer] = flugzeug
        else:
            self.__sonstigeFlugzeugMap[flugzeugnummer] = flugzeug

    def getFlugzeug(self, flugzeugnummer):
        if flugzeugnummer is None:
            return None

        if flugzeugnummer[-2:] == "TP":
            return self.__transportflugzeugMap[flugzeugnummer]
        elif flugzeugnummer[-1:] == "P":
            return self.__passagierflugzeugMap[flugzeugnummer]
        else:
            return self.__sonstigeFlugzeugMap[flugzeugnummer]
