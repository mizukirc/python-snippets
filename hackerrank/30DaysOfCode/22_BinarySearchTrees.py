class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data

class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        if root:
            height_left = self.getHeight(root.left)
            height_right = self.getHeight(root.right)
            
            if height_right > height_left:
                return height_right + 1
            else:
                return height_left + 1
        else:
            return -1
            
        print(root.data.conjugate)
        return height
    
    
T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height) 