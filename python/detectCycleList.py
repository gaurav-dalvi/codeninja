# Floyd or Brent's algorithm for this
# To read : https://en.wikipedia.org/wiki/Cycle_detection
from LinkedList import *

def detectCycle(myList):

    head = myList.head
    if head is None:
        return False

    slow = head
    fast = head
    while fast is not None and fast.getNext() is not None:
        fast = fast.getNext()
        fast = fast.getNext()
        slow = slow.getNext()
        if fast == slow:
            return True
    return False


if __name__ == '__main__':
    myList = LinkedList()
    node = Node(50)
    myList.addNodetoList(node)
    myList.addFront(40)
    node1 = Node(30)
    myList.addNodetoList(node1)
    myList.addFront(20)
    myList.addFront(10)
    node.setNext(node1)
    #myList.showList()
    print detectCycle(myList)