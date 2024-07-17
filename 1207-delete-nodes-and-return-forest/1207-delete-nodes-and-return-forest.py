# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], dl: List[int]) -> List[TreeNode]:
      
        res = []
        def dfs(n, flag):
            if not n: return None
            delete = n.val in dl
            n.left ,n.right= dfs(n.left, delete),dfs(n.right, delete) 
            if not delete and flag: res.append(n)
            return None if delete else n
        dfs(root, True)
        return res
        