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
    public String tree2str(TreeNode root) {
    
   
    if(root==null) return "";
     StringBuilder res = new StringBuilder();
    buildString(root,res);
    return res.toString();
        
    }
  private void buildString(TreeNode root, StringBuilder res){
      res.append(root.val);
      if(root.left == null && root.right==null)return;
      
          if(root.left!=null){
              res.append("(");
              buildString(root.left,res);
               res.append(")");
          }
         if(root.right!=null){
              if (root.left == null) {
                res.append("()");
            }
              res.append("(");
              buildString(root.right,res);
               res.append(")");
          }
      
  };
}