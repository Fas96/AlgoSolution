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
    public List<Double> averageOfLevels(TreeNode root) {
            List<Double> ans= new ArrayList<>();
    Queue<TreeNode> queueNode= new LinkedList<>();
    queueNode.offer(root);
    while (!queueNode.isEmpty()){
      int cnt=queueNode.size();
      double sum=0;
      for (int i = 0; i < cnt; i++) {
        TreeNode  cur=queueNode.poll();
        sum+=cur.val;
        if(cur.left!=null)queueNode.offer(cur.left);
        if(cur.right!=null)queueNode.offer(cur.right);
      }
      ans.add(sum/cnt);
    }

    return ans;
        
    }
}