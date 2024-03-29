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
     Map<String, Integer> map = new HashMap<>();
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        if(root == null) return null;
        List<TreeNode> ans = new LinkedList<>();
        postOrderTraversal(root, ans);
        return ans;

    }

    private String postOrderTraversal(TreeNode root, List<TreeNode> ans) {
        if(root == null) return "GHANA";
        String subTree = postOrderTraversal(root.left, ans) + "-" +  postOrderTraversal(root.right, ans) + "-" + root.val;
         
        map.put(subTree, map.merge(subTree, 1, Integer::sum));
        if(map.get(subTree) == 2) ans.add(root);
        return subTree;
    }
}