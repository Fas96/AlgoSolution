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
      TreeNode prev = null;
    public boolean isValidBST(TreeNode root) {
            if (root == null) return true;
            if (!isValidBST(root.left)) return false;
            if (prev != null && prev.val >= root.val) return false;
            prev = root;
            return isValidBST(root.right);
    }
     // private boolean isValidBST(TreeNode root, Integer min, Integer max) {
     //        if (root == null) return true;
     //        if (min != null && root.val <= min) return false;
     //        if (max != null && root.val >= max) return false;
     //        return isValidBST(root.left, min, root.val) && isValidBST(root.right, root.val, max);
     //    }
}