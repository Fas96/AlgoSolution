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
    public boolean hasPathSum(TreeNode root, int targetSum) {
          if(root==null) return res.size()> 0;
        Stack<Integer> stk= new Stack<>();
        getPathSum(root,targetSum,stk);
        return res.size()> 0;
    }
    
 
    
   private void  getPathSum(TreeNode root, int targetSum,Stack<Integer> stk){
        stk.push(root.val);
       
       if(root.left==null && root.right==null && root.val==targetSum) res.add(new ArrayList<>(stk));
       if(root.left!=null)getPathSum(root.left,targetSum-root.val,stk);
       if(root.right!=null)getPathSum(root.right,targetSum-root.val,stk);
       
       stk.pop();
    }
}