# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int: 
        
        if root is None: return 0
        
        q=[root]
        cnt =1
        
        while q:
            L = len(q)
            for node in range(L):
                curNode=q.pop(0)
                
                if curNode is None:
                    continue
                if not (curNode.left or curNode.right):
                    return cnt
                else:
                    q.append(curNode.left)
                    q.append(curNode.right)
                
            cnt+=1
        return cnt
                
                
        
        