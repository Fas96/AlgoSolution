# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        ptl=[] 
        def dfs(root,path):
            if root.left:
                dfs(root.left,path+str(root.val))
            if root.right:
                dfs(root.right,path+str(root.val))
            if not root.left and not root.right:
                path+=str(root.val)
                ptl.append(path)
      
        dfs(root,"")
        s=0
        for b in ptl:
            s+=int(b,2)
        return s
            
        
        