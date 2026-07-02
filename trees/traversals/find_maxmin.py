import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tree_node import TreeNode


def findMax(node):
    if node is None:
        return float('-inf')
    leftmax = findMax(node.left)
    rightmax = findMax(node.right)

    return max(leftmax , rightmax , node.data)


def findMin(node):
    if node is None:
        return float('inf')
    leftmin = findMin(node.left)
    rightmin = findMin(node.right)

    return min(leftmin , rightmin , node.data)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(10)
root.left.left.right = TreeNode(21)

maxNode = findMax(root)
minNode = findMin(root)

print(f"Max ${maxNode} Min ${minNode}")
