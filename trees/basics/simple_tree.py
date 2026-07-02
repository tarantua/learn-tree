import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tree_node import TreeNode

#Create a root 
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(root.data)
print(root.left.data)
print(root.right.data)