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

    def find_path(self, start, end, path=[]):
        """ Returns first found route
        """
        path += start
        if start not in self.lookup:
            return
        vertices = self.lookup[start]
        for v in vertices:
            if v == end:
                return v
            return self.find_path(v, end, path)

    def pprint(self):
        self.pp.pprint(self.lookup)


class GraphAdjMatrix:
    """Directed graph
    """
    pp = pprint.PrettyPrinter(indent=4)

    def __init__(self, edges: List[Tuple]) -> None:
        self.vertices = self.get_vertices(edges)
        self.matrix = self.get_matrix()
        self.add_edges(edges)

    def get_matrix(self):
        size = len(self.vertices)
        return [[0]*size for _ in range(size)]

    def has_vertice(self, vertice):
        try:
            self.vertices.index(vertice)
            return True
        except:
            return False

    def add_vertice(self, vertice):
        self.vertices.append(vertice)
        for row in self.matrix:
            row.append(0)
        self.matrix.append([0] * len(self.vertices))

    def has_edge(self, pair):
        start = self.vertices.index(pair[0])
        end = self.vertices.index(pair[1])
        return self.matrix[start][end]

    def add_edge(self, pair):
        for i in range(2):
            if not self.has_vertice(pair[i]):
                self.add_vertice(pair[i])

        if not self.has_edge(pair):
            start = self.vertices.index(pair[0])
            end = self.vertices.index(pair[1])
            self.matrix[start][end] = 1

    def add_edges(self, edges):
        for pair in edges:
            self.add_edge(pair)

    def find_path(self, start, end):
        pass

    def pprint(self):
        self.pp.pprint(self.vertices)
        self.pp.pprint(self.matrix)

    @staticmethod
    def get_vertices(edges):
        out = []
        for pair in edges:
            for i in range(2):
                if pair[i] not in out:
                    out.append(pair[i])
        return out


if __name__ == "__main__":
    graph_edges = [("Mumbai", "Paris"),
                   ("Mumbai", "Bangalore"),
                   ("Paris", "London"),
                   ("London", "Edinburgh")]
    graph = GraphAdjList(graph_edges)
    graph.pprint()

    graph_matrix = GraphAdjMatrix(graph_edges)
    graph_matrix.pprint()
    graph_matrix.add_edge(('Edinburgh', 'London'))
    graph_matrix.add_edge(('Bangalore', 'Dublin'))
    graph_matrix.pprint()