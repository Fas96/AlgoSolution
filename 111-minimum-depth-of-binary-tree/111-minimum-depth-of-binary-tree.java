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

     public int minDepth(TreeNode root) {
    if(root==null)
      return 0;
    else
      return helper(root);
  }

  private int helper(TreeNode root) {
       if(root==null)
            return Integer.MAX_VALUE;
     
    if(root!=null){
      if(root.left==null && root.right== null){
        return 1;
      }
    }
    return 1+Math.min(helper(root.left),helper(root.right));
  }
}