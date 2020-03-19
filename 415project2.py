from collections import defaultdict
import random
import pprint


class Client:
    def __init__(self, name, start, end, value):
        self.name = name
        self.start = start
        self.end = end
        self.value = value

    def description(self):
        print(self.start)
        print(self.end)
        print(self.value)


class DAG:
    def __init__(self, list):
        self.clientlist = list
        self.graph = {}
        self.buildgraph()

    def buildgraph(self):
        # double for loops to check every client
        self.graph['Start'] = []
        for elem in self.clientlist:
            for other in self.clientlist:
                if elem.end <= other.start:
                    if elem.name not in self.graph.keys():
                        self.graph[elem.name] = []
                    self.graph[elem.name].append(other.name)
            if elem.end == 100:
                if elem.name not in self.graph.keys():
                    self.graph[elem.name] = []
                self.graph[elem.name].append('End')

    def description(self):
        pprint.pprint(self.graph)


def main():
    A = Client('A', 1, 2, 5)
    B = Client('B', 2, 3, 5)
    C = Client('C', 3, 4, 5)
    D = Client('D', 4, 5, 5)
    E = Client('E', 5, 100, 5)
    list = [A, B, C, D, E]
    graph = DAG(list)
    graph.description()


main()
