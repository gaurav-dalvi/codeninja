class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

class LinkedList():

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def addFront(self, data):
        newNode = Node(data)
        newNode.setNext(self.head)
        self.head = newNode

    def addNodetoList(self, node):
        node.setNext(self.head)
        self.head = node

    def size(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.getNext()
        return count

    def showList(self):
        temp = self.head
        while temp is not None:
            print temp.getData(),
            temp = temp.getNext()
        print '\n'

    def remove(self, item):
        previous = None
        current = self.head
        found = False
        while not found and current is not None:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if found is False:
            print 'No data found'
            return
        elif previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
