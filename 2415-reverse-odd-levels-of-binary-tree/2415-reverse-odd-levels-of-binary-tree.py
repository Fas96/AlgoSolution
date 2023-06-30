# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root.left and not root.right:
            return root
        q =  [(root.left, root.right)]
        flag = True
        while q:
            level_len = len(q)
            for _ in range(level_len):
                left, right = q.pop(0) 
                if flag:
                    left.val, right.val = right.val, left.val
                if left.left: 
                    q.extend([(left.left, right.right), (left.right, right.left)])
         
            flag = True-flag
                        
        return root
        