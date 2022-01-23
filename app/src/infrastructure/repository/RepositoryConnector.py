
import mysql.connector as conn
from ..logger.LoggerService import LoggerService
from ...resources.Properties import SQL_HOST, SQL_PORT, SQL_USER, SQL_PWD, SQL_SCHEMA, SQL_SHOW, SQL_MIGRATION, \
    SQL_MIGRATION_PATH


class RepositoryConnector:
    """

    """
    def __init__(self):
        self.log = LoggerService(mClass="RepositoryConnector")
        self.conn = None
        self.props = {
            "host": SQL_HOST,
            "port": SQL_PORT,
            "user": SQL_USER,
            "pwd": SQL_PWD,
            "schema": SQL_SCHEMA,
            "showSql": SQL_SHOW,
            "migration": SQL_MIGRATION,
            "migration.path": SQL_MIGRATION_PATH
        }

    def connection(self):

        try:
            self.conn = conn.connect(user=self.props["user"],
                                     password=self.props["pwd"],
                                     host=self.props["host"],
                                     port=self.props["port"],
                                     database=self.props["schema"]
                                     )
            return self.conn
        # self.logg.info(msg=["Connection Succeded", self.conn])
        # self.conn.cursor().execute("USE {}".format(props["schema"]))
        # self.logg.info(msg=["Schema", props["schema"]])
        except conn.Error as err:
            self.log.error(msg=[err.msg])

    def executeRawQuery(self, query):
        try:
            cnx = self.connection()
            cursor = cnx.cursor()
            cursor.execute(query)
            cnx.commit()
            value = cursor.statement
            cursor.close()
            cnx.close()
            return value
        except Exception as exc:
            self.log.error(msg=[exc])

    def executeQuery(self, query):
        try:
            cnx = self.connection()
            cursor = cnx.cursor()
            cursor.execute(query)
            value = cursor.fetchone()

            cursor.close()
            cnx.close()
            return value
        except Exception as exc:
            self.log.error(msg=[exc])
        pass



