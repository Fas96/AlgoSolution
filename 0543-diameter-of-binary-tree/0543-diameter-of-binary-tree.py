# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        def getValues(n):
            if not n:
                return 0
            left = getValues(n.left)
            right = getValues(n.right)
           
            self.ans = max(self.ans, left + right)
            print(self.ans, left,right)
            return 1 + max(left, right)
        getValues(root) 
        return self.ans
            
        