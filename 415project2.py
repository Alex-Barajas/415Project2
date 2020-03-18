from collections import defaultdict

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
        self.graph = {}
        self.buildgraph()

    def buildgraph(self):
        # double for loops to check every client
        for elem in self.clientlist:
            for other in self.clientlist:
                if elem.end <= other.start:
                    if elem.name not in self.graph.keys():
                        self.graph[elem.name] = []
                    self.graph[elem.name].append(other.name)


    def description(self):
        print(self.graph)


def main():
    c1 = Client('A', 1, 2, 5)
    c2 = Client('B', 2, 3, 5)
    c3 = Client('C', 3, 4, 5)
    list = [c1, c2, c3]
    graph = DAG(list)
    graph.description()


main()
