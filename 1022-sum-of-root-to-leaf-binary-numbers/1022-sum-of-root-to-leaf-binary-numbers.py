# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    sm=0
    def sumRootToLeaf(self, root):
        
        def dfs(root,path):
            if not root:
                return 
            if not root.left and not root.right:
                path+=str(root.val)
                self.sm+=int(path,2)
            dfs(root.left,path+str(root.val))
            dfs(root.right,path+str(root.val))
        dfs(root,"")
        return self.sm
   
            
        
        