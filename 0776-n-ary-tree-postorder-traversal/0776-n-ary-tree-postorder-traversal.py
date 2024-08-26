"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:return []
        s=[root]
        ans=[]
        while s:
            cn=s.pop()
            ans.append(cn.val)
            for c in cn.children:
                s.append(c)
        return ans[::-1]
        