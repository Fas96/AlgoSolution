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

import java.util.NoSuchElementException;
class Solution {
    public List<Integer> largestValues(TreeNode root) {
    List<List<Integer>> ans = new ArrayList<>();
      dfs(ans,root,0);
    return getMaxOfEachList(ans);
    }
    private List<Integer> getMaxOfEachList(List<List<Integer>> ans)  {
        List<Integer> max = new ArrayList<>();
        for (List<Integer> list : ans) {
            max.add(list.stream()
                    .mapToInt(v -> v)
                    .max().orElseThrow(NoSuchElementException::new));
        }
        return max;
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