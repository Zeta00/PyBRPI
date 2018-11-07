import json
from websocket import create_connection

ws = create_connection("wss://wss.bithumb.com/public")
ws.connect("wss://wss.bithumb.com/public")

while True:
    result = ws.recv()
    try:
        result = json.loads(result)
        if 'data' in result.keys():
            if result['data'] != []:
                data = result['data']
                print(data)

    except:
        pass

ws.close()