
import requests

from src.ripio.RipioConstant import CONTENT_TYPE
from ..logger.LoggerService import LoggerService
from ...resources.Properties import *
import json
"""
    returns json response
"""
class RequestService:
    
    def __init__(self, baseUrl =  "https://www.google.com", contentType = {}) -> None:
        self.baseUrl = baseUrl
        self.contentType = CONTENT_TYPE if contentType != {} else contentType
        self.logger = LoggerService(debug=True, mClass = "RequestService")
        self.params = {}
        
    def getRequest(self,params = {}, baseUrl = "" ,endpoint = "/"):

        if baseUrl != "" and self.baseUrl != baseUrl:
            self.baseUrl = baseUrl
        if params != {} and self.params != params:
            self.params = params
        
        self.baseUrl += "/"+endpoint
        self.logger.logPrint(msg= ["baseUrl=",self.baseUrl,"params=",self.params])
        
        try:
            response = requests.get(self.baseUrl, self.params)
            return json.dumps(response.json(), indent=JSON_PRETTYPRINT_INDENTATION)
        except Exception as err: 
            self.logger.logPrint(err)
            return requests.HTTPError().response
        
    
























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

