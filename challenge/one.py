#!python

""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""


class Vertex(object):

    def __init__(self, vertex):
        """initialize a vertex and its neighbors

        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.id = vertex
        self.neighbors = {}

    def add_neighbor(self, vertex, weight=0):
        """adds a neighbor along a weighted edge"""
        #checks if vertex is already a neighbos
        #if not, it adds a vertex to neighbors and assigns weight
        if vertex != None:
            self.neighbors[vertex] = weight
        else:
            raise KeyError("You need a vertex!")

    def __str__(self):
        """output the list of neighbors of this vertex"""
        return str(self.id) + " adjancent to " +
        str([x.id for x in self.neighbors])

    def get_neighbors(self):
        """return the neighbors of this vertex"""
        return self.neighbors

    def get_id(self):
        """return the id of this vertex"""
        return self.id

    def get_edge_weight(self, vertex):
        """return the weight of this edge"""
        #returns the weight of the edge from this
        #vertex to the given vertex.
        return self.neighbors[vertex]

""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""


class Graph:
    def __init__(self):
        """ initializes a graph object with an empty dictionary.
        """
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        """add a new vertex object to the graph with
        the given key and return the vertex
        """
        #increments the number of vertices
        #creates a new vertex
        #adds the new vertex to the vertex list
        #returns the new vertex
        if key != None:
            self.num_vertices += 1
            new_vertex = Vertex(key)
            self.vert_list[key] = new_vertex
            return new_vertex
        raise KeyError("There's no key here")

    def get_vertex(self, n):
        """return the vertex if it exists"""
        #returns the vertex if it is in the graph
        if self.vert_list[n] != None:
            return self.vert_list[n]
        else:
            raise KeyError("It would appear the vertex you are searching for does not exist")

    def add_edge(self, f, t, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """
        #if either vertex is not in the graph, returns an error
        #if both vertices in the graph, adds the
        # edge by making t a neighbor of f
        #using the addNeighbor method of the Vertex class.
        if (get_vertex(f) != None) and (get_vertex(t) != None):
            self.vert_list[f].add_neighbor(t, cost)
            self.vert_list[t].add_neighbor(f, cost)
        else:
            raise KeyError("F or T is not found")

    def get_vertices(self):
        """return all the vertices in the graph"""
        if self.vert_list.keys() != None:
            return self.vert_list.keys()
        raise KeyError("Vertex not found")

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vert_list.values())


# Driver code


if __name__ == "__main__":

    # Challenge 1: Create the graph

    g = Graph()

    # Add your friends
    g.add_vertex("Friend 1")
    g.add_vertex("Friend 2")
    g.add_vertex("Friend 3")

    # ...  add all 10 including you ...

    # Add connections (non weighted edges for now)
    g.add_edge("Friend 1", "Friend 2")
    g.add_edge("Friend 2", "Friend 3")

    # Challenge 1: Output the vertices & edges
    # Print vertices
    print("The vertices are: ", g.get_vertices(), "\n")

    print("The edges are: ")
    for v in g:
        for w in v.get_neighbors():
            print("( %s , %s )" % (v.get_id(), w.get_id()))
