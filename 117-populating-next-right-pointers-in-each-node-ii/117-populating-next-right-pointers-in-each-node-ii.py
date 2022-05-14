class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # Empty tree
        if root == None:
            return root
        # Level order traversal keeping the track of next node in prev
        queue = [root]
        while len(queue) > 0:
            size = len(queue)
            prev = None
            while size > 0:
                node = queue.pop(0)
                size = size - 1
                node.next = prev
                prev = node
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return root