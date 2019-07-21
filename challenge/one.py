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

    def make_graph_from_file(filename):
        # Check if first line is 'G' or 'D' and store the value. If neither, raise an exception
        # For each vertex id in first line, add a vertex to the graph
        # For each of the following lines:
        # Extract the vertex ids and the (optional) weight, and add an edge to the graph
        # If it is a Graph and not a Digraph, add another edge in the opposite direction
        # Raise an exception if line contains too many (or too few) item
        raise Exception(f"File must begin with G or D, found {firstline}")

    def get_neighbors(self):
        # Make sure the input node is actually in the graph
        # Find all edges for the input node
        # See what nodes are connected to the input node via the edge
        # return the connected nodes
        pass

    def breadth_first_search(self, vertex, n):
        # Make sure the input node is actually in the graph
        # Run breadth_first_search starting from the input node and going `n` levels deep
        # Return all nodes found at the `n`th level
        pass

    def findPath(self, from_vert, to_vert):
        # Make sure that both nodes from_vert and to_vert are actually in the graph
        # Run BFS or DFS starting from from_vert
        # Figure out a way to keep track of each path you take
        # Once you find to_vert, end the search.
        # Since you've been tracking the paths, find the path that goes from from_vert to to_vert
        # Return the path, in the order of nodes visited starting with from_vert and ending with to_vert
        pass

    def find_shortest_path(self, A, B):
        # Make sure that both nodes A and B are actually in the graph
        # Run BFS starting from A
        # Figure out a way to keep track of each path you take
        # Once you find B, end the search.
        # Since you've been tracking the paths, find the shortest path that goes from A to B
        # Return the shortest path, in the order of nodes visited starting with A and ending with B
        pass

    def diameter(self):
        # For every node, find the shortest path from it to every other node in the graph and track the paths and their length
        # From your list of path/length pairs, pick the one with the largest length and return the length.
        pass

    def clique(self):
        # Start with an arbitrary vertex u and add it to the clique
        # For v in remaining vertices not in the clique
        # If v is adjacent to every other vertex already in the clique.
        # 	Add v to the clique
        # 	Discard v otherwise
        pass

    def influencer(self):
        # Create a dictionary of vertex -> PageRank value and set initial values to 1/n
        # For each iteration:
        # Create a new dictionary of vertex -> PageRank value, set all to 0
        # For each vertex v:
        # Divide up v's previous PageRank value amongst v's neighbors.
        # For m neighbors, each neighbor receives value/m
        # Replace previous PageRanks with new PageRanks
        # Sort all vertices according to their PageRank value, return sorted list
        pass

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
