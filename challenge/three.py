from two import *

"""place everything in iterable sets,
    check if already visted,
    traversing call recursively, getting as far away from node before visting"""
def dfs_r(nodes, node, visited=None):
    if visited == None:
        visited = set()
    visited.add(node)
    for i in nodes.node_dict[node] - visited:
        dfs(nodes, i, visited)
    return visited

"""place everything in iterable sets,
    check if already visted, add to stack
    traversing while stack is not empty, getting as far away from node before visting"""
def dfs_i(nodes, node):
    visited, stack = set(), [node]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(nodes.node_dict[vertex]-visited)
    return visited

"""Inspiration for code thanks to LOFAR788"""


def dijkstra_x(graph,start,goal):
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
