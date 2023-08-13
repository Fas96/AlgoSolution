# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res=[]
        q=deque([root])
        
        while q:
            sz=len(q)
            ll=deque()
            for i in range(sz):
                nd=q.popleft()
                ll.append(nd.val) if (len(res)%2==0) else ll.appendleft(nd.val)
                
                if nd.left: q.append(nd.left)
                if nd.right: q.append(nd.right)
            res.append(ll)
            
        return res
         
        
        