class TreeNode:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

#Create a root 
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(root.data)
print(root.left.data)
print(root.right.data)