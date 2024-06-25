# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def modifyBSTUtil(root, Sum): 
            if root == None:
                return 
            modifyBSTUtil(root.right, Sum)  
            Sum[0] = Sum[0] + root.val 
            root.val = Sum[0] 
            modifyBSTUtil(root.left, Sum) 
      
        modifyBSTUtil(root,[0])  
        return root