# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.parent(root)
        visited = set()
        q = [(target, 0)]
        ans = []
        while q:
            node, d = q.pop(0)
            if node in visited:
                continue
            visited.add(node)
            if d == k:
                ans.append(node.val)
                continue
            neighbors = [node.parent, node.left, node.right]
            for neighbor in neighbors:
                if neighbor:
                    q.append((neighbor, d + 1))
        return ans

    def parent(self, node, parent=None):
        if node:
            node.parent = parent
            self.parent(node.left, node)
            self.parent(node.right, node)
        