# https://www.geeksforgeeks.org/diameter-of-a-binary-tree/
# Key Learnings:
# 1: Look at the diagram above.
# 2: Watch video
# 3: So diameter could be : 1: addtion of left subtree diameter + diameter of right subbtree or
#                           2: root can not be part of diameter of tree
# 4: Write height of tree quickly without any error

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

def height_of_tree(root):
    if root is None:
        return 0

    l = height_of_tree(root.left)
    r = height_of_tree(root.right)

    if l >= r:
        return l + 1
    else:
        return r + 1

def diameter(root):

    if root is None:
        return 0

    l_ht = height_of_tree(root.left)
    r_ht = height_of_tree(root.right)

    l_diameter = diameter(root.left)
    r_diameter = diameter(root.right)

    return max((l_ht + r_ht + 1 ), max(l_diameter , r_diameter))

# def diameter_optimized(root, ans):
#     '''
#     Diameter is max of l_ht + r_ht + 1 for each node
#     '''
#     if root is None:
#         return 0
#
#     l = diameter_optimized(root.left, ans)
#     r = diameter_optimized(root.right, ans)
#     ans = max(ans, (l+r+1))
#
#     return 1 + max(l , r)


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

    print diameter(tree.root)
    # ans = 0
    # ht = diameter_optimized(tree.root, ans)
    # print ht

