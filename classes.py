import uuid
import datetime

# User
class Node:
    def __init__(self, ws, name):
        self.ws = ws
        self.id = str(uuid.uuid4())
        self.name = name
        self.links = {}

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

# Chat
class Link:
    def __init__(self, node, name, nodes):
        self.node = node
        self.id = str(uuid.uuid4())
        self.name = name
        self.nodes = nodes

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

#Message
class Message:
    def __init__(self, node, content, link):
        self.node = node
        self.id = str(uuid.uuid4())
        self.content = content
        self.link = link
        self.time = datetime.datetime.now()

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id
