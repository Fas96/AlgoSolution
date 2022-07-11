# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ls=[]
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        dq=collections.deque()
        if root:
            dq.append(root)
        res=[]
        while dq:
            size,val=len(dq),0
            for _ in range(size):
                node=dq.popleft()
                val=node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(val)
        return res
        
        