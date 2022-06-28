# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    sm=0
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        
        def dfs(node):
            if node is None:
                return
            if node.val>=low and node.val<=high:
                self.sm+=node.val
            if node.left is not None:
                dfs(node.left)
            if node.right is not None:
                dfs(node.right)
        dfs(root)
        print(self.sm)
        return self.sm