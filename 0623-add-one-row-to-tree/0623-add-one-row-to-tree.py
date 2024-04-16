# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, D: int) -> Optional[TreeNode]:
        def createBase(node):
            node=TreeNode(val)
            node.left=root
            return node
        if D==1:
            return createBase(root) 
        def createNode(node,H): 
            node.left=TreeNode(val,node.left,None)
            node.right=TreeNode(val,None,node.right)
            
        def dfs(node,H):
            if H==D-1:
                createNode(node,H) 
            if node.left:
                dfs(node.left,H+1)
            if node.right:
                dfs(node.right,H+1)
        dfs(root,1)
        return root