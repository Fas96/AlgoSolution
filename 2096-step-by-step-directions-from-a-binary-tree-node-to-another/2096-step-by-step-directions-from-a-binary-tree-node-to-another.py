# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(node, target, path):
            if not node:
                return False

            if node.val == target:
                return True

            if node.left:
                if dfs(node.left, target, path):
                    path.appendleft('L')
                    return True

            if node.right:
                if dfs(node.right, target, path):
                    path.appendleft('R')
                    return True                
            
        s_path, t_path = deque(), deque()
        dfs(root, startValue, s_path)
        dfs(root, destValue, t_path)
        
        while s_path and t_path and s_path[0] == t_path[0]:
            s_path.popleft()
            t_path.popleft()
        
        return 'U' * len(s_path) + ''.join(t_path)