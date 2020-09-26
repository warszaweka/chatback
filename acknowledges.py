# Client request acknowledgment 
import json

import data

async def create_node(node):
    datum = data.ackn_create_node(node)
    event = json.dumps(datum)
    await node.ws.send(event)

async def create_link(link):
    datum = data.ackn_create_link(link)
    event = json.dumps(datum)
    await link.node.ws.send(event)

async def send_message(message):
    datum = data.ackn_send_message(message)
    event = json.dumps(datum)
    await message.node.ws.send(event)
