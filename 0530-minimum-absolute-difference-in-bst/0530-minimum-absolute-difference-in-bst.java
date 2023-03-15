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
    public int getMinimumDifference(TreeNode root) {
           if (root == null) return 0;
         List<Integer> list = new ArrayList<>();
         dfs(root, list);
         int min = Integer.MAX_VALUE;
         for (int i = 0; i < list.size() - 1; i++) {
                min = Math.min(min, list.get(i + 1) - list.get(i));
            }

         return min;

    }

    private void dfs(TreeNode root, List<Integer> list) {
        if (root == null) return;
        dfs(root.left, list);
        list.add(root.val);
        dfs(root.right, list);
    }
}