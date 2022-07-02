# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
 
   
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ls=[]
        
        if root:
            ls.append(root.val)
        if root:
            ls+=self.preorderTraversal(root.left)
        if root:
            ls+=self.preorderTraversal(root.right)
        
        return ls
        