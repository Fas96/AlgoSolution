# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minAbsDiff = float("inf")
        prevNode = None

        def inOrderTraversal(node):
            nonlocal minAbsDiff, prevNode
            if node is None:
                return
            inOrderTraversal(node.left)
            if prevNode is not None:
                minAbsDiff = min(minAbsDiff, node.val - prevNode.val)
            prevNode = node
            inOrderTraversal(node.right)

        inOrderTraversal(root)
        return minAbsDiff