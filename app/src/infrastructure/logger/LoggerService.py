from datetime import datetime
from ...resources.Properties import *


class LoggerService:
    """
    :param mClass
    :param debug
    """
    def __init__(self, mClass="", debug=False):
        """

        :rtype: object
        """
        self.debug = DEBUG if DEBUG != debug else debug
        self.log = []
        self.mClass = mClass
        self.datetime = datetime

    def info(self, msg=[]):
        message = msg
        dateInfo = self.dateInfo()
        print("INFO", " => ", dateInfo["currDate"],
              dateInfo["currTime"], " - ", self.mClass, ": ", message)

    def error(self, msg=[]):

        message = msg
        dateInfo = self.dateInfo()
        print("ERROR", " - ", dateInfo["currDate"], dateInfo["currTime"],
              " - ", self.mClass, ": ", message)

    def dateInfo(self):
        return {
            "currTime": self.__getCurrentTime__(),
            "currDate": self.__getCurrentDate__()
        }

    def __getCurrentTime__(self):
        return self.datetime.now().time()

    def __getCurrentDate__(self):
        return self.datetime.now().date()

    def warn(self, msg):
        message = msg
        dateInfo = self.dateInfo()
        print("WARN", " - ", dateInfo["currDate"], dateInfo["currTime"],
              " - ", self.mClass, ": ", message)
