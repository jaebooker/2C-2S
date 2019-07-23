class Node(object):
    def __init__(self, data=None, pointers={}):
        self.data = data
        self.pointers = pointers
    def add_pointer(self, link):
        if link != None:
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
    def __init__(self, node1, node2, weight=0, double=False):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight
        self.double = double
    def change_weight(self, weight):
        if weight != None:
            self.weight = weight
        else:
            raise KeyError("Give it some weight!")

class Nodes(object):
    def __init__(self, nodes=[]):
        self.nodes = Set(nodes)
    def get_nodes(self):
        if self.nodes != []:
            return self.nodes
        raise KeyError("There are no nodes :( ")
    def add_node(self, node):
        if node != None:
            self.nodes.extend(node)
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

def bfs(nodes, start_node):
    visited, queue = Set(), [start_node]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(nodes[vertex]-visited)
    return visited

def bfs_paths(nodes, start_node, goal):
    queue = [(start_node),[start_node]]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in nodes[vertex] - Set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def shortest_path(nodes, start_node,goal):
    try:
        return next(bfs_paths(nodes,start_node,goal))
    except StopIteration:
        return None
#https://pastebin.com/3Q9rqGHA
#https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

def dfs(nodes, node, visited=None):
    if visited == None:
        visited = Set()
    visited.add(node)
    for i in nodes[node] - visited:
        dfs(nodes, i, visited)
    return visited

def dfs_iterative(nodes, node):
    visited, stact = Set(), [node]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(nodes[vertex]-visited)
    return visited

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
