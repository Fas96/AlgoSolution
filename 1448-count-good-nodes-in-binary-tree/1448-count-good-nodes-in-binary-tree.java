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
  
   int ans=0;
    public int goodNodes(TreeNode root) {
    if(root==null) return 0;
    if(root.left==null && root.right==null) return 1;
     goodNodesCountHelper(root, root.val);
        return ans;
  }

  private void goodNodesCountHelper(TreeNode root,int cnt) {
    if(root==null) return ;
      if(root.val>=cnt)ans++;
      goodNodesCountHelper(root.left,Math.max(cnt, root.val));
      goodNodesCountHelper(root.right,Math.max(cnt,  root.val));
       
     
  }
}