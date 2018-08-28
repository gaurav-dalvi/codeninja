from LinkedList import *

def SplitLinkedList(llist):
    evenList = LinkedList()
    oddList = LinkedList()
    fevenNode = Node()
    foddNode = Node()

    head = llist.head
    while head.getNext() is not none:
        temp = head
        data = temp.getData()
        if data % 2 == 0:

        else:



if __name__ == '__main__':
    llist = LinkedList()
    llist.addFront(20)
    llist.addFront(19)
    llist.addFront(18)
    llist.addFront(17)
    llist.addFront(16)
    llist.addFront(15)
    llist.addFront(14)
    llist.addFront(13)
    llist.addFront(12)
    llist.addFront(11)
    llist.addFront(10)
    llist.showList()