class Node(object):
    def __init__(self, data=None, pointers={}):
        """initialize a vertex and its neighbors
        pointers: pointers node is directed toward,
        data: data for given node
        """
        self.data = data
        self.pointers = pointers
    def add_pointer(self, link):
        """adds a neighbor along a weighted edge"""
        if link != None:
            self.pointers[link.node2] = link.weight
        else:
            raise KeyError("You need a link ;) ")
    def get_pointers(self):
        """return the pointers of this vertex"""
        if self.pointers != {}:
            return self.pointers
        raise KeyError("There are no pointers :( ")
    def find_link(self, node):
        """finds link, if one exists"""
        if self.pointers[node] != None:
            return self.pointers[node]
        raise KeyError("No link to this node found :'( ")

class Link(object):
    def __init__(self, node1, node2, weight=0, double=False):
        """initialize a link to its neighbors
        has two nodes for the given link
        has a given edge weight
        defines whether it is double-linked or not
        """
        self.node1 = node1
        self.node2 = node2
        self.weight = weight
        self.double = double
    def change_weight(self, weight):
        if weight != None: #changes weight, if weight exists
            self.weight = weight
        else:
            raise KeyError("Give it some weight!")

class Nodes(object):
    def __init__(self, nodes=[]):
        """initializes a nodes and its neighbors
        places nodes into a dictionary
        gets the node data for a key, storing the data of all pointers in a set
        """
        self.node_dict = {}
        for i in nodes:
            key_list = []
            for k in i.pointers.keys():
                key_list.append(k.data)
            self.node_dict[i.data] = set(key_list)
    def get_nodes(self):
        #returns nodes
        if self.node_dict != {}:
            return self.node_dict
        raise KeyError("There are no nodes :( ")
    def add_node(self, node):
        #gets the node data for a key, storing the data of all pointers in a set
        if node != None:
            key_list = []
            for k in i.pointers.keys():
                key_list.append(k.data)
            self.node_dict[node.data] = set(key_list)
        else:
            raise KeyError("You need a node >:( ")
    def node_length(self):
        return len(self.node_dict)

class Links(object):
    """Does the same thing as Nodes, except with links,
    you do not have to worry about this for now, since it is not in use yet"""
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

# def bfs_version_one(node):
#     print(node.data)
#     for k,v in node.pointers:
#         print(v)
# def bfs_version_two(nodes, node1, node2):
#     # keep track of explored nodes
#     visited = []
#     # keep track of all the paths to be checked
#     queue = [[node1]]
#
#     # return path if start is goal
#     if node1 == node2:
#         return "Node1 and Node2 are one and the same"
#
#     # keeps looping until all possible paths have been checked
#     while queue != None:
#         # pop the first path from the queue
#         path = queue.pop(0)
#         # get the last node from the path
#         current_node = path[-1]
#         if current_node not in explored:
#             neighbours = nodes[current_node]
#             # go through all neighbour nodes, construct a new path and
#             # push it into the queue
#             for neighbour in neighbours:
#                 new_path = list(path)
#                 new_path.append(neighbour)
#                 queue.append(new_path)
#                 # return path if neighbour is goal
#                 if neighbour == goal:
#                     return new_path
#
#             # mark node as explored
#             explored.append(current_node)
#     raise KeyError("We couldn't find the other node :'( ")
"""Inspiration for code thanks to Edd Mann"""


"""place everything in iterable sets,
    while the queue is not empty, add the next node to the queue,
    each time adding visted nodes to visted set
    return visted"""
def bfs(nodes, start_node):
    visited, queue = set(), [start_node]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(nodes.node_dict[vertex]-visited)
    return visited

"""place everything in iterable sets,
    while the queue is not empty, add the next node to the queue,
    traversing from start node to stop node"""
def bfs_paths(nodes, start_node, goal):
    queue = [(start_node,[start_node])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in nodes.node_dict[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

"""take bfs path, but return shortest iteration"""
def shortest_path(nodes, start_node,goal):
    try:
        return next(bfs_paths(nodes,start_node,goal))
    except StopIteration:
        return None

"""place everything in iterable sets,
    check if already visted,
    traversing call recursively, getting as far away from node before visting"""
def dfs(nodes, node, visited=None):
    if visited == None:
        visited = set()
    visited.add(node)
    for i in nodes.node_dict[node] - visited:
        dfs(nodes, i, visited)
    return visited

"""place everything in iterable sets,
    check if already visted, add to stack
    traversing while stack is not empty, getting as far away from node before visting"""
def dfs_iterative(nodes, node):
    visited, stack = set(), [node]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(nodes.node_dict[vertex]-visited)
    return visited


"""Inspiration for code thanks to LOFAR788"""


def dijkstra(graph,start,goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)

    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0,start)
    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('And the path is ' + str(path))
