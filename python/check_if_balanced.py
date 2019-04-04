# https://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/
# 1: For faster version key is to return two values and use it in the recursion
# 2: For slow version, see how in a single line return condition is designed.
#         return abs(l_ht - r_ht) <= 1 and check_if_balanced_slow(node.left) and check_if_balanced_slow(node.right)


class Node:    
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

def height(node):
    
    if node is None:
        return 0    
    l_ht = height(node.left)
    r_ht = height(node.right)
    return max(l_ht, r_ht) + 1

def check_if_balanced_slow(node):

    if node is None:
        return True
    l_ht = height(node.left)
    r_ht = height(node.right)

    return abs(l_ht - r_ht) <= 1 and check_if_balanced_slow(node.left) and check_if_balanced_slow(node.right)

def check_if_balanced_fast(node):
    
    if node is None:
        return 0, True
    
    l_ht, l_isbal = check_if_balanced_fast(node.left)
    r_ht, r_isbal = check_if_balanced_fast(node.right)
    
    return max(l_ht, r_ht) + 1, l_isbal and r_isbal and abs(l_ht - r_ht) <= 1


root = Node(10)
root.left = Node(20)
root.left.right = Node(60)
root.right = Node(30)
root.right.right = Node(70)
root.left.left = Node(40)
root.left.left.left = Node(50)
print(check_if_balanced_slow(root))
s, t = check_if_balanced_fast(root)
print(t)


        
