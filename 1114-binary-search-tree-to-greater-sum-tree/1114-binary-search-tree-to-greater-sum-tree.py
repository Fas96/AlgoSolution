# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def modifyBSTUtil(root, Sum): 
            if root == None:
                return 
            modifyBSTUtil(root.right, Sum)  
            Sum[0] = Sum[0] + root.val 
            root.val = Sum[0] 
            modifyBSTUtil(root.left, Sum) 
        def modifyBST(root):
            Sum = [0]
            modifyBSTUtil(root, Sum)
        modifyBST(root)  
        return root