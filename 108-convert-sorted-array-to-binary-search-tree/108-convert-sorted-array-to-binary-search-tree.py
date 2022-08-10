# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def dfs(lf,rt ):
            if lf > rt: return None
            mid = (lf + rt) // 2
            root = TreeNode(nums[mid])
            root.left = dfs(lf, mid - 1)
            root.right = dfs(mid+1, rt)
            return root
        
        return dfs(0, len(nums) - 1)
        