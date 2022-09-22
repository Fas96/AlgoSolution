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
     public int[] findFrequentTreeSum(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        // key: sum, value: count
        if (root == null) return new int[0];
        Map<Integer, Integer> map = new HashMap<>();
        int max = 0;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            int sum = dfs(node);
            map.put(sum, map.getOrDefault(sum, 0) + 1);
            max = Math.max(max, map.get(sum));
            if (node.left != null) queue.offer(node.left);
            if (node.right != null) queue.offer(node.right);
        }
        for (int key : map.keySet()) {
            if (map.get(key) == max) ans.add(key);
        }
        //convert list to array
        return  ans.stream().mapToInt(i->i).toArray();
    }

    private int dfs(TreeNode node) {
        if (node == null) return 0;
        int left = dfs(node.left);
        int right = dfs(node.right);
        return left + right + node.val;
    }
}