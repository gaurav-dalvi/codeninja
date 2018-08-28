from LinkedList import *

def reverseLinkedList(llist):
    prev = None
    nextNode = None
    current = llist.head
    while current is not None:
        nextNode = current.getNext()
        current.setNext(prev)
        prev = current
        current = nextNode

    llist.head = prev

if __name__ == '__main__':
    myList = LinkedList()
    node = Node(50)
    myList.addNodetoList(node)
    myList.addFront(40)
    myList.addFront(30)
    myList.addFront(20)
    myList.addFront(10)
    myList.showList()
    reverseLinkedList(myList)
    myList.showList()