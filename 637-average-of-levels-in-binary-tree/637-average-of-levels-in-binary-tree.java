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
    public List<Double> averageOfLevels(TreeNode root) {
      List<List<Integer>> levelList = new ArrayList<>();
      List<Double> res = new ArrayList<>();
     
        callStackLevels(root,levelList,0);
     
     for(List<Integer> e: levelList){
         res.add(e.stream() .mapToDouble(d -> d).average().orElse(0.0));
     }
        return res;
    }
     public void callStackLevels(TreeNode root,List<List<Integer>>  lelVals,int level) {
      if(root==null) return;
      if(level>=lelVals.size()){
        lelVals.add(new LinkedList<Integer>());
      }
      lelVals.get(level).add(root.val );
      callStackLevels(root.left,lelVals,level+1);
      callStackLevels(root.right,lelVals,level+1);
    }
}