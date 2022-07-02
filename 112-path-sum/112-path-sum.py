# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    sm=0
    r=[]
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root: return False
        
        if not root.left and not root.right:
            if root.val == targetSum:
                self.r.append(root.val)
                return True
            else:
                return False
        if self.hasPathSum(root.left,targetSum-root.val):
            self.r.append(root.val)
            return True
        if self.hasPathSum(root.right,targetSum-root.val):
            self.r.append(root.val)
            return True
        return False
                
        