from ..infrastructure.httpConnection.RequestService import RequestService
from ..infrastructure.logger.LoggerService import LoggerService
from ..infrastructure.repository.Repository import Repository
from ..resources.Properties import SQL_SCHEMA


class RipioRequestService:

    def __init__(self, baseUrl, contentType):
        if baseUrl is not None and contentType is not None:
            self.requestService = RequestService(baseUrl=baseUrl, contentType=contentType)
        self.repository = Repository()
        self.log = LoggerService(mClass="RipioRequestService")
        self.data = None

    def getDataFromApi(self, endpoint="", params={}):
        self.data = self.requestService.getRequest(
            params=params, endpoint=endpoint)
        return self.data

    def saveData(self, data, table):
        if(data is not None):

            query = "INSERT INTO `{}`.`{}` {} VALUES {}".format(
                SQL_SCHEMA,
                table,
                self.repository.columnsForInsert(data),
                self.repository.valuesConstructorForInsert(data))
            self.repository.save(query)
        else:
            self.log.warn(msg=["data:",data])

