import imp
from ..infrastructure.httpConnection.RequestService import RequestService
from ..infrastructure.logger.LoggerService import LoggerService
from .RipioConstant import *
from ..resources.Properties import *

class RipioRequestApi:
    
    def __init__(self) -> None:
        self.log = LoggerService(mClass="RipioRequestApi")
        self.conn = RequestService(baseUrl=BASE_URL, contentType=CONTENT_TYPE)
        
    def getDataFromApi(self,params = {},endpoint = ""):
        return self.conn.getRequest(params=params, endpoint=endpoint)
