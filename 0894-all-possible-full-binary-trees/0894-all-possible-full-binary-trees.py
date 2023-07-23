# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = [-1 for i in range(n+1)]
        def backtracking(i):
            if i == 1: return [TreeNode(0)]
            if not i&1: return []
            if dp[i] != -1: return dp[i]
            i -= 1
            ans = []
            for k in range(1, i+1):
                if not(k&1 and (i-k)&1): continue
                p1 = backtracking(k)
                p2 = backtracking(i-k)
                for a in p1:
                    for b in p2:
                        ans.append(TreeNode(0,a,b))
            dp[i] = ans
            return ans
        return backtracking(n)
        