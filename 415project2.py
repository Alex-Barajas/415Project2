from collections import defaultdict
import random
import pprint
import linecache


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

    def getEnd(self):
        return self.end

    def getStart(self):
        return self.start

    def getvalue(self):
        return self.value

    def getName(self):
        return self.name


class DAG:
    # pass a list of client objects to create the DAG ?
    def __init__(self, list):
        self.clientList = list
        self.clientNames = []
        self.startClients = []
        self.edges = {}
        for elem in list:
            self.clientNames.append(elem.name)
            self.edges[elem.name] = 0
        self.graph = {}
        self.buildGraph()

    def buildGraph(self):
        # double for loops to check every client
        start = self.clientNames
        for elem in self.clientList:
            for other in self.clientList:
                if int(elem.end) <= int(other.start) and elem.name != other.name:
                    if elem.name not in self.graph.keys():
                        self.graph[elem.name] = []
                    self.graph[elem.name].append(other.name)
                    self.edges[other.name] += 1
                    if other.name in start:
                        start.remove(other.name)
            if elem.name not in self.graph.keys():
                self.graph[elem.name] = []
                self.graph[elem.name].append('End')
        self.graph['Start'] = start
        self.startClients = start

    def description(self):
        # print(self.graph)
        pprint.pprint(self.graph)

    def dict(self):
        return self.graph


def top_sort(graph):
    # queue = graph.startClients
    queue = []
    result_top = []
    dict = graph.dict()
    incomingEdges = graph.edges
    for elem in incomingEdges:
        if incomingEdges[elem] == 0:
            queue.append(elem)

    while queue:
        ver = queue.pop(0)  # A
        result_top.append(ver)
        verNeighnors = dict[ver]
        for client in verNeighnors:
            if client != 'End':
                incomingEdges[client] -= 1
                if incomingEdges[client] == 0:
                    queue.append(client)
          # dequeue and append to topo sorted
    return result_top


def main():
    filename = input('En†er file name: ')
    file = open(filename)
    clientId = 'A'
    listOfClients = []
    for line in file:
        clientData = line.split()
        newClient = Client(clientId, clientData[0], clientData[1], clientData[2])
        clientId = chr(ord(clientId) + 1)
        # clientId += 1
        listOfClients.append(newClient)
    graph = DAG(listOfClients)
    print('\nDAG Dictionary:')
    graph.description()
    print("\nTop Sort: ")
    print(top_sort(graph))


main()
