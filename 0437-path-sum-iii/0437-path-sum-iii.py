# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.cnt=0
        def sm(no,ts):
            if no is None:
                return
            if no.val==ts:
                self.cnt+=1
            sm(no.left,ts-no.val)
            sm(no.right,ts-no.val)
        def dfs(node,tg):
            if node is None:
                return

            sm(node,tg)
            dfs(node.left,tg)
            dfs(node.right,tg)
        dfs(root,targetSum)
        return self.cnt