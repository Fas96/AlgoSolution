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
       ArrayList<Integer> ar=new ArrayList<>();
    int i=0;
    public void recoverTree(TreeNode root) {
       traverse(root);
        Collections.sort(ar);
        build(root);
    }
    void build(TreeNode root){
        if(root==null)
            return;
        build(root.left);
        root.val=ar.get(i);
        i++;
        build(root.right);
    }
    void traverse(TreeNode root){
        if(root==null)
            return ;
        traverse(root.left);
         ar.add(root.val);
        traverse(root.right);
    }
}