# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.to=[]
       
        def dfs(node,arr):
            if node:
                if not node.left and not node.right: 
                    self.to.append([node.val]+arr)
                    arr=[]
                    return

                dfs(node.left,[node.val]+arr)
                dfs(node.right,[node.val]+arr)
        dfs(root,[])
        paths = [['abcdefghijklmnopqrstuvwxyz'[val] for val in path] for path in self.to] 
        paths = [''.join(path) for path in paths] 
        return min(paths )