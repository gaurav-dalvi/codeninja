# Print binary tree in level by level fashion
# https://www.geeksforgeeks.org/level-order-tree-traversal/
# https://www.youtube.com/watch?v=13m9ZCB8gjw&t=15s - Video
# https://www.geeksforgeeks.org/print-level-order-traversal-line-line/
# Algorithm:
# 1: if root is null then return
# 2: create empty queue and then insert root node in it
# 3: Run loop till queue is not Empty
# 4: remove from queue and print
# 5: add left children and add right children
#
# Key learnings :
# 1: Implement Binary tree fast in python
# 2: Remember why we added return in find_path function. In True case you need to return all the way to previous callers
# 3: To get address of any object in python use id(object) function
# 4: There is no need to write insert function. you can just manually create binary tree
# 5: In find_path add every node in path and then in the end remove it (WHY remove it, dry run with example)
# 6: Use     python list as Queue, no need to import anything
# adding into Queue : q.append()
# removing from queue: q.pop(0)
# 7: Read height of tree code as well here
# 8: To print tree level by level on new line,  node_count (queue size) indicates number of nodes at current level.

import Queue

class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def get_children(self):
        children = []
        if self.left != None:
            children.append(self.left)
        if self.right != None:
            children.append(self.right)

        return children

class BinaryTree(object):

    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = Node(value)

    def print_tree(self):
        self._print_tree(self.root)

    def _print_tree(self, curr_node):

        if curr_node is not None:
            self._print_tree(curr_node.left)
            print(curr_node.value),
            self._print_tree(curr_node.right)

def find_path(curr_node, node, path):
    if curr_node is None:
        return False
    path.append(curr_node.value)
    if curr_node.value == node.value:
        return True

    if (curr_node.left and find_path(curr_node.left, node, path)) or (curr_node.right and find_path(curr_node.right, node, path)):
        return True

    path.pop()
    return False

def print_tree_by_level_straight(root):
    # BFS traversal of tree or graph
    if root is None:
        print ''
    q = Queue.Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        print node.value,
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)

    print ''

def print_tree_by_level_new_line(root):

    if root is None:
        print ''

    q = Queue.Queue()
    q.put(root)

    while(True):
        node_count = q.qsize()
        if node_count == 0:
            break

        while node_count > 0:
            node = q.get()
            print node.value,
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
            node_count -= 1
        print ''


def height_of_tree(root):
    if root is None:
        return 0
    else:
        l = height_of_tree(root.left)
        r = height_of_tree(root.right)
        if l >= r:
            return l + 1
        else:
            return r + 1

if __name__ == '__main__':

    tree = BinaryTree()
    tree.set_root(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    tree.root.right.right.right = Node(8)
    tree.root.left.left.left = Node(9)
    tree.print_tree()
    print ''
    print 'Height of tree is : ', height_of_tree(tree.root)
    path = []
    if find_path(tree.root, tree.root.right.left, path):
        print path
    print ''
    print_tree_by_level_new_line(tree.root)

    print ''
    print_tree_by_level_straight(tree.root)
