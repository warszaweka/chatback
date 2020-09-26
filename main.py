#!/usr/bin/python
# WebSocket Server
import asyncio
import websockets
import json

import commands

async def handler(ws, path):
    node = None
    try:
        async for event in ws:
            data = json.loads(event)
            print(data)
            if data["type"] == "comm":
                if data["subtype"] == "createNode":
                    node = await commands.create_node(ws, data)
                elif data["subtype"] == "createLink":
                    await commands.create_link(node, data)
                elif data["subtype"] == "sendMessage":
                    await commands.send_message(node, data)
    finally:
        if node:
            await commands.kill_node(node)

server = websockets.serve(handler, "localhost", 8080)
asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()
