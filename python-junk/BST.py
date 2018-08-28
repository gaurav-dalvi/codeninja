class Node():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setData(self,newdata):
        self.data = newdata

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.left = right

    def getData(self):
        return self.data

class BST():

    def __init__(self):
        self.head = None

    def InorderBST(self, head):
        self.head = head
        if head is not None:
            self.InorderBST(head.getLeft())
            print head.getData(),
            self.InorderBST(head.getRight())
        print '\n'

    def PreorderBST(self, head):
        self.head = head
        if head is not None:
            print head.getData(),
            self.PreorderBST(head.getLeft())
            self.PreorderBST(head.getRight())
        print '\n'

    def PostorderBST(self, head):
        self.head = head
        if head is not None:
            self.PostorderBST(head.getLeft())
            self.PostorderBST(head.getRight())
            print head.getData(),
        print '\n'

    def SearchBST(self, node):
        head = self.head
        if head.getData() == node.getData():
            return True
        else:
            return (self.SearchBST(node.getLeft()) and self.SearchBST(node.getRight()))


if '__name__' == '__main__':
    head = Node(10)
    node1 = Node(20)
    node2 = Node(5)

    head.setLeft(node2)
    head.setRight(node1)

    head.InorderBST()