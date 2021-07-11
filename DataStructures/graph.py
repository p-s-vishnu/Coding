"""
Three way to represent graphs - objects and pointers, matrix, and adjacency list.
Know the pros and cons of each representation
"""
from typing import List, Tuple
import pprint


class GraphAdjList:
    """ Better for Sparse graphs but time consuming to find edge
    """
    pp = pprint.PrettyPrinter(indent=4)

    def __init__(self, edges: List[Tuple]):
        self.edges = edges
        self.lookup = {}
        self.build_graph()

    def add(self, pair: Tuple):
        if pair[0] in self.lookup:
            self.lookup[pair[0]].add(pair[1])
        else:
            self.lookup[pair[0]] = {pair[1]}

    def build_graph(self):
        for pair in self.edges:
            self.add(pair)

    def find_shortest_edge(self, start, end):
        """ Returns first found route
        """
        pass

    def pprint(self):
        self.pp.pprint(self.lookup)


class GraphAdjMatrix:
    def __init__(self, edges):
        self.edges = edges


if __name__ == "__main__":
    graph_edges = [("Mumbai", "Paris"),
                   ("Mumbai", "Bangalore"),
                   ("Paris", "London")]
    graph = GraphAdjList(graph_edges)
    graph.pprint()
