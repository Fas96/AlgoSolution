# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children = collections.defaultdict(list)
        has_parent = collections.defaultdict(lambda: False)
        
        for p, c, l in descriptions:
            children[p].append((c, l))
            has_parent[c] = True
            has_parent[p] |= False
            
        root_val = next(k for k, v in has_parent.items() if not v)
        
        def construct(node_val):
            node = TreeNode(node_val)
            
            for c, l in children[node_val]:
                new_node = construct(c)
                
                if l:
                    node.left = new_node
                else:
                    node.right = new_node

            return node
            
        return construct(root_val)