# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        levelTraversed = []

        def bfs(Node): 
            if not Node:
                return
            queueUse = deque([Node])
            while queueUse:
                tempLevelValues = []
                
                for n in range(len(queueUse)):
                    curLement = queueUse.popleft() 
                    if curLement:
                        tempLevelValues.append(curLement.val)
                        queueUse.append(curLement.left)
                        queueUse.append(curLement.right)
                        
                if tempLevelValues:
                    levelTraversed.append(tempLevelValues)
        
        bfs(root)
        levelSum = float("-inf")
        heightOfLevel = 0 
        
        for idx in range(len(levelTraversed)):
            temp=sum(levelTraversed[idx]) 
            if temp>levelSum:
                levelSum = max(levelSum,temp)
                heightOfLevel = idx + 1 
        return heightOfLevel 