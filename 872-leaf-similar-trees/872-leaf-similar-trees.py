# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
 
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        rt1=[]
        rt2=[]
        def dfs(node,l):
            if not node:
                return
            if not node.left and not node.right:
                l.append(node.val)
            dfs(node.left,l)
            dfs(node.right,l)

        dfs(root1,rt1)
        dfs(root2,rt2)
        
        return rt1==rt2