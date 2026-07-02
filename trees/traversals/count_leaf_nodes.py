import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tree_node import TreeNode

def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

def countLeafNodes(node):
    if node is None:
        return 0
    if node.left is None or node.right is None:
        return 1
    
    left_count = countLeafNodes(node.left)
    right_count = countLeafNodes(node.right)

    return left_count+right_count

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(10)
root.left.left.right = TreeNode(21)


totalNodeCount = countLeafNodes(root)
print(totalNodeCount)