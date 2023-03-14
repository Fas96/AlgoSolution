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
     List<List<Integer>> pathValues = new ArrayList<>();
    public int sumNumbers(TreeNode root) {
        if (root == null) return 0;
        // return sumNumbersOP(root, 0);
        List<Integer> path = new ArrayList<>();
        dfs(root, path);
       
        int sum = 0;
        for (List<Integer> pathValue : pathValues) {
            int pathSum = 0;
            for (int i = 0; i < pathValue.size(); i++) {
                pathSum += pathValue.get(i) * Math.pow(10, pathValue.size() - i - 1);
            }
            sum += pathSum;
        }
        return sum;

    }

    private void dfs(TreeNode root, List<Integer> path) {
        if (root == null) return;
        path.add(root.val);
        if (root.left == null && root.right == null) {
            pathValues.add(new ArrayList<>(path));
        }
        dfs(root.left, path);
        dfs(root.right, path);
        path.remove(path.size() - 1);
    }
    
       
     //can use this

    // private int sumNumbersOP(TreeNode root, int sum) {
    //     if (root == null) return 0;
    //     sum = sum * 10 + root.val;
    //     if (root.left == null && root.right == null) return sum;
    //     return sumNumbers(root.left, sum) + sumNumbers(root.right, sum);
    // }
}