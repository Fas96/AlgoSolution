# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ls=[]
        if root:
            ls+=self.postorderTraversal(root.left)
            ls+=self.postorderTraversal(root.right)
            ls.append(root.val)
        return ls
            
        