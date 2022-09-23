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
    public int findBottomLeftValue(TreeNode root) {
   
   List<List<Integer>> ans = new ArrayList<>();
      dfs(ans,root,0);
        List<Integer> last=ans.get(ans.size()-1);
    return last.get(0);
    }
   
    
     public void dfs(List<List<Integer>>  lelVals,TreeNode root,int level) {
      if(root==null) return;
      if(level>=lelVals.size()){
        lelVals.add(new LinkedList<Integer>());
      }
      lelVals.get(level).add(root.val );
      dfs(lelVals,root.left,level+1);
      dfs(lelVals,root.right,level+1);
    }
    
    
    
      
}