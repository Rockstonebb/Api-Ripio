import asyncio
import websockets
import base64
import json
TOPIC = 'wss://api.exchange.ripio.com/ws/v2/consumer/non-persistent/public/default/orderbook_btc_usdc/suscription-1'
TOPIC2 = 'wss://api.exchange.ripio.com/ws/v1/'
async def orderbook_consumer():
    async with websockets.connect(TOPIC2) as websocket:
        while True:
            msg = await websocket.recv()
            data = json.loads(msg)
            print(base64.b64decode(data['payload']))
            ack = {'messageId': data['messageId']}
            await websocket.send(ack)
asyncio.get_event_loop().run_until_complete(orderbook_consumer())