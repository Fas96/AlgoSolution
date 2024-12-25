# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = deque([root]) 
        ans = []
        while q:
            size = len(q)
            nodes = [] 
            for _ in range(size):
                node = q.popleft()
                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    nodes.append(node.val)
             
            ans += [max(nodes)]
        
        return ans