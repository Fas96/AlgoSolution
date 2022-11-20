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
   public List<List<Integer>> closestNodes(TreeNode root, List<Integer> queries) {
   TreeSet<Integer> treeSet = new TreeSet<>();
        dfs(root, treeSet);
        List<List<Integer>> answer = new ArrayList<>();
        for (Integer query : queries) {
            Integer first = treeSet.floor(query);
            Integer second = treeSet.ceiling(query);
            answer.add(List.of(
                    first == null ? -1 : first
                    , second == null ? -1 : second)
            );
        }
        return answer;


}

    private void dfs(TreeNode root, TreeSet<Integer> all) {
        if (root == null) return;
        dfs(root.left, all);
        all.add(root.val);
        dfs(root.right, all);
    }

     
}