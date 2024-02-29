# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool: 
        q = collections.deque()
        q.append(root)
        IDX = 0
        E_O = True
        
        while q:
            LVAL = []
            qLen = len(q)
            
            for i in range(qLen):
                node = q.popleft()
                
                if node:
                    if IDX % 2 == 0 and node.val % 2 == 0:
                        E_O = False
                    elif IDX % 2 != 0 and node.val % 2 != 0:
                        E_O = False
                        
                    LVAL.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                
            if LVAL:
                if IDX % 2 == 0 and LVAL != sorted(list(set(LVAL))):
                    E_O = False
                    break
                    
                elif IDX % 2 != 0 and LVAL !=  sorted(list(set(LVAL)))[::-1]:
                    E_O = False
                    break
                
            IDX += 1
            
        return E_O