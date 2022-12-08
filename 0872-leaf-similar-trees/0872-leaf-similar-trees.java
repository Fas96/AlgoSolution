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
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        
   
       if (root1 == null && root2 == null) return true;
        if (root1 == null || root2 == null) return false;

        List<Integer> tree1 =  new LinkedList<>(); 
        List<Integer> tree2 =  new LinkedList<>();  

        dfs(root1, tree1);
        dfs(root2, tree2);
        
        return tree1.equals(tree2);
         
    }

    private void dfs(TreeNode root1, List<Integer> ll) {
        if (root1 == null) return;
        if (root1.left == null && root1.right == null) {
            ll.add(root1.val);
            return;
        }
        dfs(root1.left, ll);
        dfs(root1.right, ll);
    }
}