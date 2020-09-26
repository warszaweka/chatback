import state

def updt_new_node(node):
    return {"type": "updt",
            "subtype": "newNode",
            "payload": {"name": node.name,
                        "id": node.id,},}

def updt_new_link(link):
    return {"type": "updt",
            "subtype": "newLink",
            "payload": {"node": link.node.id,
                        "id": link.id,
                        "name": link.name,
                        "nodes": [i_node.id for i_node in link.nodes.values()],},}

def updt_recieved_message(message):
    return {"type": "updt",
            "subtype": "recievedMessage",
            "payload": {"node": message.node.id,
                        "id": message.id,
                        "content": message.content,
                        "link": message.link.id,
                        "time": str(message.time),},}

def updt_new_message(message):
    return {"type": "updt",
            "subtype": "newMessage",
            "payload": {"node": message.node.id,
                        "id": message.id,
                        "link": message.link.id,
                        "time": str(message.time)},}

def updt_dead_node(node):
    return {"type": "updt",
            "subtype": "deadNode",
            "payload": {"id": node.id,},}


def ackn_create_node(node):
    return {"type": "ackn",
            "subtype": "createNode",
            "payload": {"id": node.id,
                        "nodes": [{"id": i_node.id,
                                   "name": i_node.name,} for i_node in state.nodes.values() if i_node != node],
                        "links": [{"node": i_link.node.id,
                                   "id": i_link.id,
                                   "name": i_link.id,
                                   "nodes": [j_node.id for j_node in i_link.nodes.values()],} for i_link in state.links.values()],},};

def ackn_create_link(link):
    return {"type": "ackn",
            "subtype": "createLink",
            "payload": {"id": link.id,},}

def ackn_send_message(message):
    return {"type": "ackn",
            "subtype": "sendMessage",
            "payload": {"id": message.id,
                        "time": str(message.time),}}
