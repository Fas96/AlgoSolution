# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return
        q=deque([root])
        res=deque()
        while q:
            sz=len(q)
            tz=[]
            for i in range(sz):
                nd=q.popleft()
                tz.append(nd.val)
                if nd.left: q.append(nd.left)
                if nd.right: q.append(nd.right)
            res.appendleft(tz)
        return res
                
        