# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q=deque()
        q.append(root)
        an=[[root.val]]
        while q: 
            ll=len(q)
            larr=[]
            for _ in range(ll):
                cur=q.popleft() 
                if cur.left:
                    q.append(cur.left)
                    larr.append(cur.left.val)
                if cur.right:
                    q.append(cur.right)
                    larr.append(cur.right.val)
            if len(larr)>0:
                an.append(larr)
        return an
        