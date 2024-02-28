# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    val = float('inf')
    height = 0
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode],height: int):

            if not root:
                return None

            left, right = dfs(root.left,height + 1), dfs(root.right, height + 1)
                
            if root and height > self.height and not (root.left or root.right):
                self.height = height
                self.val = root.val

            return root
        
        dfs(root, self.height)

        return self.val if self.height > 0 else root.val 
        