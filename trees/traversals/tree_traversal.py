import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tree_node import TreeNode

def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

#preorder
def recursion1(node):
    if node is None:
        return
    print(node.data)
    recursion1(node.left)
    recursion1(node.right)

#inorder
def recursion2(node):
    if node is None:
        return
    recursion2(node.left)
    print(node.data)
    recursion2(node.right)

#postorder
def recursion3(node):
    if node is None:
        return
    recursion3(node.left)
    recursion3(node.right)
    print(node.data)


root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Preorder")
recursion1(root)

print("Inorder")
recursion2(root)

print("Postorder")
recursion3(root)