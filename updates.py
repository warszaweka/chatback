import json
import asyncio

import data
import state

async def new_node(node):
    datum = data.updt_new_node(node)
    event = json.dumps(datum)
    sends = [i_node.ws.send(event) for i_node in state.nodes.values() if i_node != node]
    if sends:
        await asyncio.wait(sends)

async def new_link(link):
    datum = data.updt_new_link(link)
    event = json.dumps(datum)
    sends = [i_node.ws.send(event) for i_node in state.nodes.values() if i_node != link.node]
    if sends:
        await asyncio.wait(sends)

async def recieved_message(message):
    datum = data.updt_recieved_message(message)
    event = json.dumps(datum)
    sends = [i_node.ws.send(event) for i_node in message.link.nodes.values() if i_node != message.node]
    if sends:
        await asyncio.wait(sends)

async def new_message(message):
    datum = data.updt_new_message(message)
    event = json.dumps(datum)
    sends = [i_node.ws.send(event) for i_node in state.nodes.values() if i_node not in message.link.nodes.values()]
    if sends:
        await asyncio.wait(sends)

async def dead_node(node):
    datum = data.updt_dead_node(node)
    event = json.dumps(datum)
    sends = [i_node.ws.send(event) for i_node in state.nodes.values()]
    if sends:
        await asyncio.wait(sends)
