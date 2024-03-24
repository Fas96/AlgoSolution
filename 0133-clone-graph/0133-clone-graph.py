"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:return None
        def dfs(node):
            nw=Node(node.val)
            mp[nw.val]=nw
            for n in node.neighbors:
                if n.val in mp:
                    nw.neighbors.append(mp[n.val])
                    continue
                nw.neighbors.append(dfs(n))
            return nw
            
        mp={}
        return dfs(node)
        