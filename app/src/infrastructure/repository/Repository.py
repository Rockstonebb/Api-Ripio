from .RepositoryConnector import RepositoryConnector
from .RepositoryConstants import *
from ..logger.LoggerService import LoggerService
import re

"""
SQL Connection Properties

SQL_HOST = "localhost"
SQL_PORT = 3306
SQL_USER = "root"
SQL_PWD = "mysql"
SQL_SCHEMA = "awesome_app"
SQL_SHOW = True

"""


class Repository:

    def __init__(self):
        self.conn = RepositoryConnector()
        self.log = LoggerService(mClass="Repository")

    def migrate(self):
        pass

    def getConfig(self,property):
        try:
            rs = self.conn.executeQuery("SELECT c.value FROM ripio_app.configs c where c.name = '"+property+"';")
            return rs[0]

        except Exception as ex:
            self.log.error(ex)

    def save(self, query):
        try:
            self.log.info(self.conn.executeRawQuery(query))
        except Exception as ex:
            self.log.error(ex)

    def valuesConstructorForInsert(self, data):
        query = "("
        curr = 0
        max = len(data) - 1
        for x in data:
            if (max != curr):
                query += self.__validate__(data[x]) + ", "
                curr += 1
            else:
                query += self.__validate__(data[x])
        return query + ");"

    def columnsForInsert(self, data):
        query = "("
        curr = 0
        max = len(data) - 1
        for x in data:
            if (max != curr):
                query += x + ", "
                curr += 1
            else:
                query += x
        return query + ")"

    def __validate__(self, param):
        # Check if is a DATETIME
        if (re.fullmatch(REGEX_DATETIME + REGEX_DECIMALS, string=param)):
            return "'" + re.split(REGEX_DECIMALS, param)[0] + "'"
        # Check if is a VARCHAR
        if (re.fullmatch("([^0-9]*$)", param)):
            return "'" + param + "'"
        return param
