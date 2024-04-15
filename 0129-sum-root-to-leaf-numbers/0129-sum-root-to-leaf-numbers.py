# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.arr=[]
        def dfs(node,ls):
            if node:
                if not node.left and not node.right:
                    self.arr.append(ls+[node.val])
                dfs(node.left,ls+[node.val])
                dfs(node.right,ls+[node.val])
        dfs(root,[])
   
        def convert(list): 
            s = [str(i) for i in list] 
            res = int("".join(s))
            return(res)
        ans=0
        for x in self.arr:
            ans+=convert(x)
        return ans 