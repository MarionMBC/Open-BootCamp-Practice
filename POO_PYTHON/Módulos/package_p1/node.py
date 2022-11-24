class node:
    def __init__(self, val):
        self.val = val
        self.next = None


class linkedList:
    def __init__(self):
        self.first = None

    def addNode(self, val):
        newNode = node(val)
        if self.first is None:
            self.first = newNode
        else:
            current = self.first
            while current.next:
                current = current.next
            current.next = newNode


    def printNodes (self):
        nodes = []
        if self.first is None:
            return "list is empty"
        else:
            current = self.first
            while current is not None:
                nodes.append(current.val)
                current = current.next
        return print(nodes)


class main ():
    if __name__ == '__main__':
        list = linkedList()
        list.addNode(4)
        list.addNode(5)
        list.addNode(7)
        list.addNode(8)
        list.printNodes()
