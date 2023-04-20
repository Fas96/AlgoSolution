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
    public int widthOfBinaryTree(TreeNode root) {
     if(root==null) return 0;
        List<LinkedList<Integer>> list = new ArrayList<>();
        helper(root,0,0,list);
        int max=0;
        for (LinkedList<Integer> integers : list) {
            max=Math.max(max,integers.getLast()-integers.getFirst()+1);
        }
        return max;
    }

    private void helper(TreeNode root, int i, int i1, List<LinkedList<Integer>> list) {
        if(root==null) return;
        if(list.size()==i){
            list.add(new LinkedList<>());
        }
        list.get(i).add(i1);
        helper(root.left,i+1,2*i1,list);
        helper(root.right,i+1,2*i1+1,list);
    }
}