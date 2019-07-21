"""Now we do it my way"""

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.pointers = {}
    def add_pointer(self, link):
        if node != None:
            self.pointers[link.node2] = link.weight
        else:
            raise KeyError("You need a link ;) ")
    def get_pointers(self):
        if self.pointers != {}:
            return self.pointers
        raise KeyError("There are no pointers :( ")
    def find_link(self, node):
        if self.pointers[node] != None:
            return self.pointers[node]
        raise KeyError("No link to this node found :'( ")

class Link(object):
    def __init__(self, node1, node2, weight=0):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight
    def change_weight(self, weight):
        if weight != None:
            self.weight = weight
        else:
            raise KeyError("Give it some weight!")

class Nodes(object):
    def __init__(self, nodes=[]):
        self.nodes = nodes
    def get_nodes(self):
        if self.nodes != []:
            return self.nodes
        raise KeyError("There are no nodes :( ")
    def add_node(self, node):
        if node != None:
            self.nodes.append(node)
        else:
            raise KeyError("You need a node >:( ")
    def node_length(self):
        return len(self.nodes)

class Links(object):
    def __init__(self, links=[]):
        self.links = links
    def get_links(self):
        if self.links != []:
            return self.links
        raise KeyError("There are no links :( ")
    def add_link(self, link):
        if link != None:
            self.links.append(link)
        else:
            raise KeyError("You need a link >:( ")
    def link_length(self):
        return len(self.links)

def bfs(node):
    print(node.data)
    for k,v in node.pointers:
        print(v)
