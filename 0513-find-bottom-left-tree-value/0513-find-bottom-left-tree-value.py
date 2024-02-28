# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        self.val = float('inf')
        self.H = 0
        def dfs(root,h):
            if not root: return None
            L, R = dfs(root.left,h + 1), dfs(root.right, h + 1)
            if root and h > self.H and not (root.left or root.right):
                self.H = h
                self.val = root.val

            return root
        
        dfs(root, self.H)

        return self.val if self.H > 0 else root.val 
        