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
  
    int res=0;
 
    public int goodNodes(TreeNode root) {
    if(root==null) return 0;
    if(root.left==null && root.right==null) return 1;
  
    goodNodesCountHelper(root,root.val);
    return res;
  }

  private void goodNodesCountHelper(TreeNode root,int curVal) {
    if(root==null) return;
     if(root.val>=curVal)res++;
      goodNodesCountHelper(root.left,Math.max(curVal,root.val));
   
      goodNodesCountHelper(root.right,Math.max(curVal,root.val));
       
    
     
  }
}