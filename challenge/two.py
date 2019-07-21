"""Now we do it my way"""

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.pointers = {}
    def add_pointer(self, link):
        if node != None:
            self.pointers[link.node2] = link.weight
        else:
            raise KeyError("You need a link! ;) ")
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

class Links(object):
    def __init__(self, links=[]):
        self.links = []
    def get_links(self):
        if self.links != []:
            return self.links
        else:
            raise KeyError("No links found :( ")
    def add_link(self, link):
        if link != None:
            self.links.append(link)
        else:
            raise KeyError("You need a link >:( ")
