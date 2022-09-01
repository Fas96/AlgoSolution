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
  
   
    public int goodNodes(TreeNode root) {
    if(root==null) return 0;
    if(root.left==null && root.right==null) return 1;
    return goodNodesCountHelper(root, -100000);
  }

  private int goodNodesCountHelper(TreeNode root,int cnt) {
    if(root==null) return 0;
      int ans=root.val>=cnt?1:0;
      ans+=goodNodesCountHelper(root.left,Math.max(cnt,root.val));
      ans+=goodNodesCountHelper(root.right,Math.max(cnt,root.val));
      return ans;
     
  }
}