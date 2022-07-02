# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        newNode=TreeNode(val)
        if root is None:
            return newNode
        parent,current=None,root
        
        while current is not None:
            parent=current
            
            if current.val<= val:
                current=current.right
            else:
                current=current.left
        if parent.val<= val:
            parent.right=newNode
        else:
            parent.left=newNode
        return root
            

        