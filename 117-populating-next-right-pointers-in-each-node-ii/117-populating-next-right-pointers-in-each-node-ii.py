class Solution:
    from collections import deque
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 
        queue = deque()
        queue.append([root, 0])
        prev, lvl = None, -1
        while queue:
            current, level = queue.popleft()
            if current.left:
                queue.append([current.left, level + 1])
            if current.right:
                queue.append([current.right, level + 1])
            if prev and level == lvl:
                prev.next = current
            prev, lvl = current, level
        return root  