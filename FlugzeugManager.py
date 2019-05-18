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
            if flugzeugnummer in self.__transportflugzeugMap:
                return self.__transportflugzeugMap[flugzeugnummer]
        elif flugzeugnummer[-1:] == "P":
            if flugzeugnummer in self.__passagierflugzeugMap:
                return self.__passagierflugzeugMap[flugzeugnummer]
        else:
            if flugzeugnummer in self.__sonstigeFlugzeugMap:
                return self.__sonstigeFlugzeugMap[flugzeugnummer]
