# Lowest common ancestor in binary tree or BST
# https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/ - For python BST code
# https://www.youtube.com/watch?v=13m9ZCB8gjw&t=15s - Video
# Key learnings :
# 1: Implement Binary tree fast in python
# 2: Two approaches for this problem
# 	1: Print path and then find latest common for two nodes (How will you print path from node to root)
# 	2: Return null or return node to its parent as explained in Video
# 3: Remember why we added return in find_path function. In True case you need to return all the way to previous callers
# 4: To get address of any object in python use id(object) function

class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def set_value(self,value):
        self.value = value

    def get_children(self):
        children = []
        if self.left is not None:
            children.append(self.left)
        if self.right is not None:
            children.append(self.right)

        return children


class BST(object):

    def __init__(self):
        self.root = None

    def _set_root(self, value):
        self.root = Node(value)

    def insert(self, value):
        if self.root is None:
            self._set_root(value)
        else:
            self._insert_node(self.root, value)

    def _insert_node(self, curr_node, value):

        if curr_node.value >= value:
            if (curr_node.left):
                self._insert_node(curr_node.left, value)
            else:
                curr_node.left = Node(value)
        else:
            if (curr_node.right):
                self._insert_node(curr_node.right, value)
            else:
                curr_node.right = Node(value)

    def print_tree(self):
        self._print_tree_inorder(self.root)

    def _print_tree_inorder(self, curr_node):
        # printing tree in inorder fashion
        # call using root node
        if curr_node is not None:
            self._print_tree_inorder(curr_node.left)
            print curr_node.value,
            self._print_tree_inorder(curr_node.right)


def find_path(node, val, path):
    if node == None:
        return False
    if node.value == val:
        path.append(node.value)
        return True
    elif val < node.value:
        # go to left of the tree
        path.append(node.value)
        return find_path(node.left, val, path)
    else:
        path.append(node.value)
        return find_path(node.right, val, path)


# Run time O(n)
# Space O(n)
def LCA_1(tree, val1, val2):
    path1 = []
    path2 = []

    if find_path(tree.root, val1, path1) and find_path(tree.root, val2, path2):
        # now find LCA by traversing from two paths
        index = 0
        while index < len(path1) and index < len(path2):
            if path1[index] == path2[index]:
                lca = path1[index]
            index += 1
    else:
        raise Exception('Invalid input')

    return lca


# Run time O(n)
# Space O(constant)
def LCA_2(tree, val1, val2):
    # this function returns Node object
    return _LCA_2(tree.root, val1, val2)


def _LCA_2(node, val1, val2):
    if node is None:
        return None

    if node.value == val1 or node.value == val2:
        return node

    left = _LCA_2(node.left, val1, val2)
    right = _LCA_2(node.right, val1, val2)

    if left != None and right != None:
        return node
    if left == None and right == None:
        return None

    if left != None:
        return left
    elif right != None:
        return right


if __name__ == '__main__':
    tree = BST()
    tree.insert(3)
    tree.insert(6)
    tree.insert(2)
    tree.insert(11)
    tree.insert(9)
    tree.insert(5)
    tree.insert(8)
    tree.insert(13)
    tree.insert(7)
    tree.print_tree()
    print ''
    print LCA_2(tree, 7, 11).value
