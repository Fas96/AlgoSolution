# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr=[]
        def po(root):
            
            if root and root.left:
                po(root.left)
            if root and root.right:
                po(root.right)
            if root:
                arr.append(root.val)
        po(root)
        return arr