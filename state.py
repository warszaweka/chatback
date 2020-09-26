# Server state changes
import classes

nodes = {}
links = {}

def create_node(ws, data):
    node = classes.Node(ws, data["payload"]["name"])
    nodes[node.id] = node
    return node

def create_link(node, data):
    a_nodes = {}
    for i_node in data["payload"]["nodes"]:
        a_nodes[i_node] = nodes[i_node]
    a_nodes[node.id] = node
    link = classes.Link(node, data["payload"]["name"], a_nodes)
    links[link.id] = link
    for i_node in a_nodes.values():
        i_node.links[link.id] = link
    return link

def send_message(node, data):
    message = classes.Message(node, data["payload"]["content"], links[data["payload"]["link"]])
    return message

def kill_node(node):
    for i_link in node.links.values():
        del links[i_link.id]
        for j_node in i_link.nodes.values():
            if j_node != node:
                del j_node.links[i_link.id]
    del nodes[node.id]
