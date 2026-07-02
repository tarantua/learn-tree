#trust me this is not easy as it seems, recursion is a tricky problem
#understand how the call stack operates in a recursive problem 

#     1
#    / \
#   2   3

#call stack for the above tree looks like this 

# count(1)
# │
# ├── count(2)
# │      │
# │      ├── count(None) → 0
# │      └── count(None) → 0
# │
# │      returns 1 ( 1 + ....... - this is that 1 , 1+0+0 , see now it makes sense , taadaa!!!)
# │
# ├── count(3)
# │      │
# │      ├── count(None) → 0
# │      └── count(None) → 0
# │
# │      returns 1
# │
# returns 3 ( 1 + 1 + 1)



import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tree_node import TreeNode

def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

def countTotalNodes(node):
    if node is None:
        return 0
    left_count = countTotalNodes(node.left)
    right_count = countTotalNodes(node.right)

    return 1+left_count+right_count

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(10)
root.left.left.right = TreeNode(21)


totalNodeCount = countTotalNodes(root)
print(totalNodeCount)