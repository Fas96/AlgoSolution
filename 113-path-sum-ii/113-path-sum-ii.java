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
  List<List<Integer>>  res= new ArrayList<>();


  public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
    if(root==null)return res;
    Stack<Integer> stkTrack = new Stack<>();
    getPathSum(root,targetSum,stkTrack);
    return res;
  }

  private void getPathSum(TreeNode root, int targetSum, Stack<Integer> stkTrack) {
    stkTrack.push(root.val);
    if(root.left==null && root.right==null && targetSum==root.val)res.add(new ArrayList<>(stkTrack));
    if(root.left!=null)getPathSum(root.left,targetSum-root.val,stkTrack);
    if(root.right!=null)getPathSum(root.right,targetSum-root.val,stkTrack);
    stkTrack.pop();
  }
}