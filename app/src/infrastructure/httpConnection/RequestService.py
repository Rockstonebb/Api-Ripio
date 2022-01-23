
import requests

from src.ripio.RipioConstant import CONTENT_TYPE
from ..logger.LoggerService import LoggerService
from ...resources.Properties import *
import json
from ..repository.Repository import Repository
"""
    returns json response
"""


class RequestService:

    def __init__(self, baseUrl="https://www.google.com", contentType={}) -> None:
        self.baseUrl = baseUrl
        self.contentType = CONTENT_TYPE if contentType != {} else contentType
        self.log = LoggerService(debug=True, mClass="RequestService")
        self.params = {}
        self.repo = Repository()
        self.endpoint = "/"

    def getRequest(self, params={}, endpoint=""):

        if endpoint != "/" :
            endpoint = self.baseUrl+"/"+endpoint
        self.log.info(
            msg=["baseUrl=",endpoint, "params=", params])

        try:
            response = requests.get(endpoint, params)

            if(JSON_PRETTYPRINT is True):
                return json.dumps(response.json(), indent=JSON_PRETTYPRINT_INDENTATION)
            return response.json()

        except Exception as err:
            self.log.error(err)
            return requests.HTTPError().response

    def clearCache(self):
        self.params = {}
        self.endpoint = "/"

# import socketio

# sio = socketio.Client()

# @sio.on('connect')
# def on_connect():
#     print('connection established')
#     msg = {
#         "method": "GET",
#         "params": [
#             "trades@BTC_USDC",
#             "orderbook@BTC_USDC",
#             "rate@BTC_USDC"
#         ]
#     }
#     sio.emit('message', msg)

# @sio.on('message')
# def on_message(data):
#     print('message received with ', data)

# @sio.on('disconnect')
# def on_disconnect():
#     print('disconnected from server')

# sio.connect('wss://api.exchange.ripio.com/ws/v1/')
# sio.wait()
