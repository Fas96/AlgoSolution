# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        self.res = []
        
        def dfs(node: TreeNode, path: List[int], pathSum: int):
            if not node.left  and not node.right:
                if sum(path) + node.val == targetSum:
                    self.res.append(path + [node.val])
            
            if node.left:
                dfs(node.left, path + [node.val], pathSum + node.val)
            if node.right:
                dfs(node.right, path + [node.val], pathSum + node.val)
        
        dfs(root, [], 0) 
        return self.res
        