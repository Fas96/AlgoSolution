# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        nodes=collections.defaultdict(list)
        q=[(root,0,0)]
        print(nodes)
        
        while q:
            node,level,parent=q.pop(0)
            nodes[node.val]=[level,parent]
            
            if node.left:
                q.append((node.left,level+1,node.val))
            if node.right:
                q.append((node.right,level+1,node.val))
        if nodes[x][0]==nodes[y][0] and nodes[x][1]!=nodes[y][1]:
            return True
        return False