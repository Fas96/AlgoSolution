# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q=deque()
        q.append(root)
        an=[[root.val]]
        mx=1
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
                if mx%2==0:
                    an.append(larr)
                else:
                    an.append(larr[::-1])
                    
            mx+=1
        return an
        