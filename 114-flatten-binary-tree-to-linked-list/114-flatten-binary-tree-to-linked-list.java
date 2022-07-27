/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    
    public void flatten(TreeNode root) {
        if(root==null){
            return;
        }
       Stack<TreeNode> pushVisitedOnStack = new Stack<TreeNode>();
        pushVisitedOnStack.push(root);
        
        while(!pushVisitedOnStack.isEmpty()){
            TreeNode curNode=pushVisitedOnStack.pop();
            
            //maintaining the preorder traversal by 
            //first visiting right and left
            if(curNode.right!=null){
                pushVisitedOnStack.push(curNode.right);
            }
             if(curNode.left!=null){
                pushVisitedOnStack.push(curNode.left);
            }
            //pushing on right
            if(!pushVisitedOnStack.isEmpty()){
                curNode.right=pushVisitedOnStack.peek();
                curNode.left=null;
            }
            
        }
       
        
    }
}