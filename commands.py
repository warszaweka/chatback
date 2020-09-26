# Handling client requests
import state
import acknowledges
import updates

async def create_node(ws, data):
    node = state.create_node(ws, data)
    await acknowledges.create_node(node)
    await updates.new_node(node)
    return node

async def create_link(node, data):
    link = state.create_link(node, data)
    await acknowledges.create_link(link)
    await updates.new_link(link)
    return link

async def send_message(node, data):
    message = state.send_message(node, data)
    await acknowledges.send_message(message)
    await updates.recieved_message(message)
    await updates.new_message(message)
    return message

async def kill_node(node):
    state.kill_node(node)
    await updates.dead_node(node)
