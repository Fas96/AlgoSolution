# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        leafs = []
        parents = dict()
        q = deque()
        q.append((root, None))
        
        while q:
            node, parent = q.popleft()
            
            parents[node] = parent
            if not node.left and not node.right:
                leafs.append(node)
            
            if node.left:
                q.append((node.left, node))
                
            if node.right:
                q.append((node.right, node))
                
        
        ans = float('-inf')
        
        for node in leafs:
            maxAtPath = float('-inf')
            minAtPath = float('inf')
            
            p = node
            while p:
                maxAtPath= max(maxAtPath, p.val)
                minAtPath= min(minAtPath, p.val)
                p = parents[p]
            
            ans = max(ans, abs(minAtPath- maxAtPath))
        
    
        return ans
        