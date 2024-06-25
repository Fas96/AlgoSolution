# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum=0
    def bstToGst(self, root: TreeNode) -> TreeNode:
         
        def modifyBSTUtil(root): 
            if root == None: return 
            modifyBSTUtil(root.right)  
            self.sum = self.sum + root.val 
            root.val = self.sum
            modifyBSTUtil(root.left) 
      
        modifyBSTUtil(root)  
        return root