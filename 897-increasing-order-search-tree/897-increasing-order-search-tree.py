# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
   
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        r=[]
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            r.append(node.val)
            dfs(node.right)
            
        dfs(root)

        ntn=TreeNode(r[0])
        ctn=ntn
        
        for v in r:
            ctn.right=TreeNode(v)
            ctn=ctn.right
        return ntn.right
        