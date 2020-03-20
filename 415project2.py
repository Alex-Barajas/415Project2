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
        self.clientlist = list
        self.clientNames = []
        for elem in list:
            self.clientNames.append(elem.name)
        self.graph = {}
        self.buildgraph()

    def buildgraph(self):
        # double for loops to check every client
        start = self.clientNames
        for elem in self.clientlist:
            for other in self.clientlist:
                if elem.end <= other.start:
                    if elem.name not in self.graph.keys():
                        self.graph[elem.name] = []
                    self.graph[elem.name].append(other.name)
                    if other.name in start:
                        start.remove(other.name)
                        
            if elem.name not in self.graph.keys():
                self.graph[elem.name] = []
                self.graph[elem.name].append('End')
        self.graph['Start'] = start

    def description(self):
        print(self.graph)
        # pprint.pprint(self.graph)

#class topGraph: # we might not need this
        #def __init__(self, vertices):
        #self.V = vertices
        #self.graph = defaultdict() # how can we use the graph we already created ?

def top_sort(graph):
    queue = []
    result_top = []

    # first create graph and generate each in-degree
    for u in graph:
        in_degree_count[u] = 0

    #in_degree_count = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]: # process every edge
            in_degree_count[v] += 1

    # queue all nodes with indegree =0
    for i in in_degree_count:
        if in_degree_count[i] == 0:
            queue.append(i)

    visited_count = 0 # visited vertices might not need this
    # store the topo sorted
    while queue:
        ver = queue.pop(0)
        result_top.append(ver) # dequeue and append to topo sorted

        for neighbor in graph[ver]: # go thru all neighbors nodes of ver, decrease their in-degree by 1
            in_degree_count[neighbor] -= 1
            if in_degree_count[neighbor] == 0:
                queue.append(neighbor)


        visited_count +=1
    return result_top




def main():
    filename = input('En†er file name ')
    file = open(filename)
    clientId = 0
    listofClients = []
    for line in file:
        clientData = line.split()
        newClient = Client(clientId, clientData[0],  clientData[1],  clientData[2])
        # Clientname = chr(ord(Clientname) + 1)
        clientId += 1
        listofClients.append(newClient)
    graph = DAG(listofClients)
    graph.description()


main()
