# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res, prev, curStreak, maxStreak = [], None, 0, -1
        
        def dfs(node):
            if not node: return
            nonlocal prev, curStreak, maxStreak
            
            dfs(node.left)
            
            if node.val == prev:
                curStreak += 1
            else:
                prev = node.val
                curStreak = 1
            
            if curStreak == maxStreak:
                res.append(node.val)
            elif curStreak > maxStreak:
                res.clear()
                res.append(node.val)
                maxStreak = curStreak

            dfs(node.right)

        dfs(root)

        return res
        