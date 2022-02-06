from .RipioRequestService import RipioRequestService
from ..infrastructure.logger.LoggerService import LoggerService
from .RipioConstant import *


class RipioRequestApi:

    def __init__(self) -> None:
        self.log = LoggerService(mClass="RipioRequestApi")
        self.requestService = RipioRequestService(
            baseUrl=BASE_URL, contentType=CONTENT_TYPE)
        self.data = None

    def getDataFromApi(self, endpoint, table):
        self.requestService.saveData(self.requestService.getDataFromApi(endpoint=endpoint), table=table)

