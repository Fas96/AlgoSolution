# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return
        q=deque([root])
        res=[]
        while q:
            sz=len(q)
            tm=[]
            for i in range(sz):
                node=q.popleft()
                tm.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                
            res.append(sum(tm)/len(tm))
        return res
        