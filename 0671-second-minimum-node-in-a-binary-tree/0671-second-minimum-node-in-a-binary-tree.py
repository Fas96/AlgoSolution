# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.ans=[]
        
        def dfs(node):
            if not node: return
            self.ans.append(node.val)
            dfs(node.left)
            dfs(node.right)
           
        dfs(root)
        self.ans.sort()
        arr=list(set(self.ans))
        ans=-1
        arr.sort()
        for i in range(len(arr)):
            if i+1==2:
                ans=arr[i]

        return ans
            
        