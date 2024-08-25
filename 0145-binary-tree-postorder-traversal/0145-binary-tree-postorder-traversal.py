# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return root
        
        head=root
        ans=[]
        def go(va):
            
            if va and va.left:
                go(va.left)
            if va and va.right:
                go(va.right)
            if va:
                ans.append(va.val)
        go(root)
        return ans
