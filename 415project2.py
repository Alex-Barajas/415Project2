class Client:
    def __init__(self, start, end, value):
        self.start = start
        self.end = end
        self.value = value

    def descrition(self):
        print(self.start)
        print(self.end)
        print(self.value)

    def getEnd(self):
        return self.end

    def getStart(self):
        return self.start

    def getvalue(self):
        return self.value

class DAG:
    # pass a list of client objects to create the DAG ?
    def __init__(self, listOfClient):
        self.clients = listOfClient
        self.graph = {}

    def buildgraph(self):
        # double for loops to check every client
        for i in self.clients:
            for j in self.clients:
                if self.clients[i].getEnd <= self.clients[j].getStart:
                    print("found")
def main():
    c1 = Client(1, 2, 5)
    c2 = Client(2, 3, 5)
    c3 = Client(3, 4, 5)
    list = [c1, c2, c3]
    graph = DAG(list)
    c1.descrition()
    c2.descrition()
    c3.descrition()


main()
