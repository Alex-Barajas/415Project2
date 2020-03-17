class Client:
    def __init__(self, start, end, value):
        self.start = start
        self.end = end
        self.value = value

    def descrition(self):
        print(self.start)
        print(self.end)
        print(self.value)


class DAG:
    def __init__(self):
        pass

def main():
    c1 = Client(1, 2, 5)
    c2 = Client(2, 3, 5)
    c3 = Client(3, 4, 5)
    c1.descrition()
    c2.descrition()
    c3.descrition()


main()
