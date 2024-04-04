# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr=[]
        def dfs(root):
            if root:
                arr.append(root.val)
            if root and root.left:
                dfs(root.left)
            if root and root.right:
                dfs(root.right)
        dfs(root) 
        return arr