import asyncio
import websocket
import json
import secret

WS_URI = secret.WS_URI


async def handler(token):
    ws = websocket.create_connection(WS_URI.format(token=token))
    while True:
        msg = ws.recv()
        print(token)
        print(msg)

        await asyncio.Future()

with open('jwt_list.json', 'r') as file:
    jwt_list = json.load(file)

tokens = jwt_list


async def main():
    tasks = []
    for token in tokens:
        tasks.append(handler(token))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
