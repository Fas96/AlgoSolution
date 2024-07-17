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
            toDelete = n.val in dl
            n.left = dfs(n.left, toDelete)
            n.right = dfs(n.right, toDelete)
            if not toDelete and flag: res.append(n)
            return None if toDelete else n
        dfs(root, True)
        return res
        