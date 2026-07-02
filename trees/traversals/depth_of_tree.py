import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tree_node import TreeNode


def depthofTree(node):
    if node is None:
        return -1 # remember this is where I got confused , if -1 is retured , depth is calculated based on the edges , if the nodes need to be calculated always consider 0.
    
    left = depthofTree(node.left)
    right = depthofTree(node.right)

    return 1 + max(left , right)


#Create a root 
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(10)
root.left.left.right = TreeNode(21)

depthTree = depthofTree(root)
print(depthTree)