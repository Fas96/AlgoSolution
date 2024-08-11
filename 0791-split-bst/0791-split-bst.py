# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        def dfs(node):
            if not node:return
            if node.val<=target:
                return dfs(node.right)
            else:
                node.left=dfs(node.left)
                node.right=dfs(node.right)
            return node
        def bfs(node):
            if not node:return
            if node.val>target:
                return bfs(node.left)
            else:
                node.left=bfs(node.left)
                node.right=bfs(node.right)
            return node
        v1=dfs(deepcopy(root))
        v2=bfs(deepcopy(root))
        return [v2,v1]
        