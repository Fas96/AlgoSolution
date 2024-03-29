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
    public TreeNode pruneTree(TreeNode root) {
        return dfs(root);
        
    }
    private TreeNode dfs(TreeNode root){
         if(root==null) return null;
        root.left=dfs(root.left);
        root.right=dfs(root.right);
        // return   (root.val == 1 || root.left != null || root.right != null) ? root : null;
        
        return (root.val==0 && root.left==null && root.right==null)?null:root;
        
        }
}