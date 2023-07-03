"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None: return 0
        
        q=[root]
        
        cnt=0
        
        while q:  
            size = len(q)
            for i in range(size):
                curNode = q.pop(0)
                if curNode.children:
                    for curNode in curNode.children:
                        q.append(curNode)
            cnt+=1
        return cnt 
        