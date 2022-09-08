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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> lstVals= new ArrayList<>();
        if(root==null) return lstVals;
        inorderTraversal(root,lstVals);
        return lstVals;
    }
  private void  inorderTraversal(TreeNode root,List<Integer> lstVals){
    if(root==null) return;
    
    
    inorderTraversal(root.left,lstVals);
      lstVals.add(root.val);
    inorderTraversal(root.right,lstVals);
    
}
}