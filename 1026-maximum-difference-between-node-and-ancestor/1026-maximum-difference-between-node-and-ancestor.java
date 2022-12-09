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
    public int maxAncestorDiff(TreeNode root) {
         HashMap<Integer, LinkedList<TreeNode>> nodeAndAncestors = new HashMap<>();
        int max = 0;
        LinkedList<TreeNode> ancestors = new LinkedList<>();
        ancestors.add(root);
        nodeAndAncestors.put(root.val, ancestors);
        LinkedList<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            LinkedList<TreeNode> nodeAncestors = nodeAndAncestors.get(node.val);
            if (node.left != null) {
                LinkedList<TreeNode> leftAncestors = new LinkedList<>(nodeAncestors);
                leftAncestors.add(node.left);
                nodeAndAncestors.put(node.left.val, leftAncestors);
                queue.add(node.left);
            }
            if (node.right != null) {
                LinkedList<TreeNode> rightAncestors = new LinkedList<>(nodeAncestors);
                rightAncestors.add(node.right);
                nodeAndAncestors.put(node.right.val, rightAncestors);
                queue.add(node.right);
            }
        }
        for (LinkedList<TreeNode> ancestorList : nodeAndAncestors.values()) {
            int min = Integer.MAX_VALUE;
            int max2 = Integer.MIN_VALUE;
            for (TreeNode ancestor : ancestorList) {
                if (ancestor.val < min) min = ancestor.val;
                if (ancestor.val > max2) max2 = ancestor.val;
            }
            int diff = max2 - min;
            if (diff > max) max = diff;
        }
        return max;
    }
}