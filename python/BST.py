class TreeNode():

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
        self.root = None

    def getRoot(self):
        return self.root

    def insertBST(self, data):
        Node temp = Node(data)
        if self.root is None:
            self.root = temp
            return root
        else:
            curr_data = self.root.getData()
            if curr_data