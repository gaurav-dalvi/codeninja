from LinkedList import *

# Find kth from last element in the given Linked List
def FindLastNthElement(llist, n):
    size = llist.size()
    if size < n or n <= 0:
        print 'Invalid value of n = %s' % (n)
        return None
    count = 1
    first = llist.head
    second = llist.head
    while count != n:
        second = second.getNext()
        count += 1

    while second.getNext() != None:
        second = second.getNext()
        first = first.getNext()
    return first

if __name__ == '__main__':
    myList = LinkedList()
    myList.addFront(50)
    myList.addFront(40)
    myList.addFront(30)
    myList.addFront(20)
    myList.addFront(10)
    myList.showList()
    temp = FindLastNthElement(myList, 1)
    # need to handle if temp is none or not.
    print temp.getData()
