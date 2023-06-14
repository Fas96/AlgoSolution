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
    private int minAbsDiff;
    private TreeNode prevNode;

    public int getMinimumDifference(TreeNode root) {
        minAbsDiff = Integer.MAX_VALUE;
        prevNode = null;

        inOrderTraversal(root);

        return minAbsDiff;
    }

    private void inOrderTraversal(TreeNode node) {
        if (node == null) {
            return;
        }

        inOrderTraversal(node.left);

        if (prevNode != null) {
            minAbsDiff = Math.min(minAbsDiff, node.val - prevNode.val);
        }

        prevNode = node;

        inOrderTraversal(node.right);
    }
}