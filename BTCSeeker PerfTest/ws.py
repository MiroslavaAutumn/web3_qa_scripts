import asyncio
import json
import secret
import websockets

with open("jwt_list.json", "r") as file:
    jwt_list = json.load(file)

WS_URI = secret.WS_URI


async def ws(jwt):
    async with websockets.connect(WS_URI.format(token=jwt)) as websocket:
        async for message in websocket:
            print(message)


async def main():
    tasks = []
    for token in jwt_list:
        tasks.append(asyncio.create_task(ws(token)))
    await asyncio.gather(*tasks)


asyncio.run(main())
