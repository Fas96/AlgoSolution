# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ls=[]
        if root:
            ls=self.inorderTraversal(root.left)
            ls.append(root.val)
            ls+=self.inorderTraversal(root.right)
        
        return ls
        