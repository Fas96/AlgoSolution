# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements(object):
    
    def __init__(self, root): 
        self.groot=TreeNode()
        self.sets=set()
        
        if root is not None and root.val==-1:
            root.val=0   
            self.sets.add(root.val) 

        self.solve(root)
        self.groot=root



    def solve(self, node): 
        if node is None:
            return
        
        if node.left is not None:
            node.left.val=2*node.val+1;   
            self.sets.add(node.left.val); 
        
        if node.right is not None:
            node.right.val=2*node.val+2;   
            self.sets.add(node.right.val); 
        
        self.solve(node.left)
        self.solve(node.right)        



    def find(self, target): 
        if target in self.sets:
            return True
        
        return False

 