# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int: 
        
        def recursive_bfs(queue, depth):
            if not queue:
                return depth

            nextLevel = []
            for node in queue:
                if node is None:
                    continue
                if not (node.left or node.right):
                    return depth
                else:
                    nextLevel.append(node.left)
                    nextLevel.append(node.right)

            return recursive_bfs(nextLevel, depth + 1)

        if root is None:
            return 0

        return recursive_bfs([root], 1)
        
                
                
        
        