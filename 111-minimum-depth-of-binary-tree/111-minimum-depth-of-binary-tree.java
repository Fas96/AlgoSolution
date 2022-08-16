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

public int minDepth(TreeNode root) {
    if (root == null)
      return 0;
    else {
      Queue<TreeNode> queue = new LinkedList<TreeNode>();
      queue.offer(root);
      int level = 1;
      int i, N;
      TreeNode current;
      while (!queue.isEmpty()) {
        N = queue.size();
        for (i = 0; i < N; i++) {
          current = queue.poll();
          if (current.left == null && current.right == null)
            return level;

          if (current.left != null)
            queue.offer(current.left);

          if (current.right != null)
            queue.offer(current.right);
        }

        ++level;
      }

      return -1;
  }
}
}