# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:

        tree_map = {}
        parent_set = set()
        child_set = set()
        for (parent,child,relation) in descriptions:
            parent_set.add(parent)
            child_set.add(child)
            parent_node = None
            if parent in tree_map:
                parent_node = tree_map[parent]
            else:
                parent_node = TreeNode(parent,left=None,right=None)
                tree_map[parent]=parent_node

            child_node =None
            if child in tree_map :
                child_node = tree_map[child]
            else:
                child_node = TreeNode(child,left=None,right=None)
                tree_map[child] = child_node
            if relation == 1:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
        return tree_map[(parent_set-child_set).pop()]