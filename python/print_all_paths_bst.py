# https://www.geeksforgeeks.org/given-a-binary-tree-print-out-all-of-its-root-to-leaf-paths-one-per-line/
# Focus on why we are popping from the stack at the end
class Node():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST():

    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        if self.root == None:
            self.root = node
        else:
            temp = self.root
            parent = None
            while temp != None:
                parent = temp
                if temp.data > data:
                    temp = temp.left
                else:
                    temp = temp.right
            if parent.data > data:
                parent.left = node
            else:
                parent.right = node
    
    def inorder(self, root):
        if root == None:
            return
        else:
            self.inorder(root.left)
            print root.data,
            self.inorder(root.right)

    def preorder(self, root):
        if root == None:
            return
        else:
            print root.data,
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root == None:
            return
        else:
            self.postorder(root.left)
            self.postorder(root.right)
            print root.data,

    def r_insert(self, data):
        if self.root == None:
            self.root = Node(data)
            return
        else:
            self._r_insert(self.root, data)

    def _r_insert(self, root, data):

        if root.data > data:
            if root.left == None:
                root.left = Node(data)
                return
            else:
                self._r_insert(root.left, data)
        else:
            if root.right == None:
                root.right = Node(data)
                return
            else:
                self._r_insert(root.right, data)
        
def print_all_paths(root, path):
    if root == None:
        return
    else:
        path.append(root.data)
        if root.left == None and root.right == None:
            print(path)
        
        print_all_paths(root.left, path)
        print_all_paths(root.right, path)
        path.pop()
        
bst = BST()
bst.r_insert(50)
bst.r_insert(40)
bst.r_insert(70)
bst.r_insert(30)
bst.r_insert(45)
bst.r_insert(80)
bst.r_insert(65)
print_all_paths(bst.root, [])

