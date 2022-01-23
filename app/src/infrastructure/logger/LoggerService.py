from datetime import datetime
from ...resources.Properties import *

class LoggerService:
    def __init__(self,debug = False , mClass = ""):
        self.debug = DEBUG
        self.log = []
        self.type = "INFO"
        self.mClass = mClass
        self.datetime = datetime
    
    def logPrint(self,msg = []):
        currTime = self.__getCurrentTime__()
        currDate = self.__getCurrentDate__()
        message  = msg
        print( self.type, " => ",currDate , currTime," - " ,self.mClass, ": ", message)
        print()
        

    def __getCurrentTime__ (self):
        return self.datetime.now().time()
        
    def __getCurrentDate__ (self):
        return self.datetime.now().date()

        