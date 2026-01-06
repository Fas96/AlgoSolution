# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int: 
        def bfs(root):
            if not root:
                return []

            r = []
            q = deque([root])   

            while q:
                ls = len(q)
                cln = [] 
                for _ in range(ls):
                    node = q.popleft()
                    cln.append(node.val) 
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right) 
                r.append(cln)

            return r
         
        ans=float("-inf")
        rans=1
        prev=-1
        for i, v in enumerate(bfs(root)):
            ans=max(ans,sum(v))
            if ans>prev:
                rans=i+1 
            prev=ans
        return rans

        