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
    public List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> ans = new ArrayList<>();
      callStackLevels(ans,root,0);
    return ans;
    }
    
     public void callStackLevels(List<List<Integer>>  lelVals,TreeNode root,int level) {
      if(root==null) return;
      if(level>=lelVals.size()){
        lelVals.add(new LinkedList<Integer>());
      }
      lelVals.get(level).add(root.val );
      callStackLevels(lelVals,root.left,level+1);
      callStackLevels(lelVals,root.right,level+1);
    }
}