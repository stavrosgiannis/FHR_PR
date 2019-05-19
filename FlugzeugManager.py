class FlugzeugManager():

    __referenz = None

    def __init__(self):
        self.__passagierflugzeugMap = {}
        self.__transportflugzeugMap = {}
        self.__sonstigeFlugzeugMap = {}

    @staticmethod
    def getReferenz():
        if FlugzeugManager.__referenz == None:
            FlugzeugManager.__referenz = FlugzeugManager()
        return FlugzeugManager.__referenz

    def addFlugzeug(self, flugzeug):
        if flugzeug == None or not flugzeug.istFlugzeugGueltig():
            return False

        flugzeugnummer = flugzeug.getFlugzeugnummer()

        if flugzeugnummer[-2:] == "TP":
            self.__transportflugzeugMap[flugzeugnummer] = flugzeug
        elif flugzeugnummer[-1:] == "P":
            self.__passagierflugzeugMap[flugzeugnummer] = flugzeug
        else:
            self.__sonstigeFlugzeugMap[flugzeugnummer] = flugzeug

    def getFlugzeug(self, flugzeugnummer):
        if flugzeugnummer == None:
            return None

        if flugzeugnummer[-2:] == "TP":
            return self.__transportflugzeugMap[flugzeugnummer]
        elif flugzeugnummer[-1:] == "P":
            return self.__passagierflugzeugMap[flugzeugnummer]
        else:
            return self.__sonstigeFlugzeugMap[flugzeugnummer]
