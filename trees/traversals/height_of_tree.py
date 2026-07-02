import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tree_node import TreeNode


def heightOfTree(node):
    if node is None:
        return -1

    left_height = heightOfTree(node.left)
    right_height = heightOfTree(node.right)

    return  1 + max(left_height , right_height)

#Create a root 
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

height = heightOfTree(root)
print(height)