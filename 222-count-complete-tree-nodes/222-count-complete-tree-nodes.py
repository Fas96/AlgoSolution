# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
 
    def countNodes(self, root):
        if not root:
            return 0
        l=self.countNodes(root.left) 
        r=self.countNodes(root.right)
        return l+r+1
        
        