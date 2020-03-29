from collections import defaultdict
import random
import linecache


class Client:
    def __init__(self, name, start, end, value):
        self.name = str(name)
        self.start = start
        self.end = end
        self.value = int(value)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

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
        self.end = Client('End', 0, 0, 0)
        self.start = Client('Start', 0, 0, 0)
        for elem in list:
            self.clientNames.append(elem.name)
            self.edges[elem.name] = 0
        self.graph = {}
        self.buildGraph()

    def buildGraph(self):
        # double for loops to check every client
        start = self.clientList.copy()
        for elem in self.clientList:
            for other in self.clientList:
                if int(elem.end) <= int(other.start) and elem.name != other.name:
                    if elem.name not in self.graph.keys():
                        self.graph[elem.name] = []
                    self.graph[elem.name].append(other)
                    self.edges[other.name] += 1
                    if other in start:
                        start.remove(other)
            if elem.name not in self.graph.keys():
                self.graph[elem.name] = []
                self.graph[elem.name].append(self.end)
        self.graph['Start'] = start
        self.startClients = start

    def description(self):
        print(self.graph)

    def dict(self):
        return self.graph

    def Neighbors(self, client):
        return self.graph[client]

    def getClient(self, client):
        for elem in self.clientList:
            if elem.name == client:
                return elem


def top_sort(graph):
    queue = []
    result_top = []
    dict = graph.dict()
    incomingEdges = graph.edges
    for elem in incomingEdges:
        if incomingEdges[elem] == 0:
            queue.append(graph.getClient(elem))
    while queue:
        ver = queue.pop(0)  # A
        result_top.append(ver)
        verNeighnors = dict[ver.name]
        for client in verNeighnors:
            if client.name != 'End':
                incomingEdges[client.name] -= 1
                if incomingEdges[client.name] == 0:
                    queue.append(client)
    return result_top


def optPath(topList, graph):
    # dict = graph.dict()
    # numClients = len(graph.clientList)
    # # templist = [0] * numClients

    # This portion of the function assigned the maxium value a vertex
    # can achieve based on its neighbors values, makes use of a tempDict
    tempDict = {}
    for client in graph.clientList:
        tempDict[client] = 0
    for vertex in reversed(list(topList)):
        vertexNeighbor = graph.Neighbors(vertex.name)  # get the neighbors of vertex
        vertexValue = vertex.value  # saves value of the vextex
        if vertexNeighbor[0].name != 'End':
            for Neighbor in vertexNeighbor:  # find the neighbor that makes him richest
                tempMax = vertex.value + tempDict[Neighbor]
                if tempMax > vertexValue:
                    vertexValue = tempMax
        tempDict[vertex] = vertexValue

    # Using out Temp Dictionary and the orginal DAG we can cross reference to find the optimal path
    # can start at the start nodes and then go to the its largest neighbor etc etc
    solution = []
    startlist = graph.startClients
    max = maxClient(startlist, tempDict)
    solution.append(max)
    while max.name != 'End':
        max = maxClient(graph.Neighbors(max.name), tempDict)
        if max.name == 'End':
            continue
        solution.append(max)
    print('\nOptimal revenue earned is ', tempDict[solution[0]])
    print('Clients contributing to this optimal revenue: ', end='')
    for elem in solution:
        if elem != solution[-1]:
            print(elem, end=', ')
        else:
            print(elem)


def maxClient(list, dict):
    maxitem = list[0]
    if maxitem.name == 'End':
        return maxitem
    for elem in list:
        if dict[elem] > dict[maxitem]:
            maxitem = elem
    return maxitem


def main():
    filename = input('Enter the file to read data: ')
    file = open(filename)
    clientId = 1
    listOfClients = []
    for line in file:
        clientData = line.split()
        newClient = Client(clientId, clientData[0], clientData[1], clientData[2])
        # clientId = chr(ord(clientId) + 1)
        clientId += 1
        listOfClients.append(newClient)
    print("\nThere are ", len(listOfClients), " clients in this file")
    DAGGraph = DAG(listOfClients)
    # print('\nDAG Dictionary:')
    graph = DAGGraph.dict()
    # print(graph)
    # print("\nTop Sort: ")
    topList = (top_sort(DAGGraph))
    # print(topList)
    optPath(topList, DAGGraph)


main()
