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
    public int sumNumbers(TreeNode root) {
      List<List<Integer>> hold=  pathSum(root);
      
      int res=resultFromList(hold);
      return res;
    }
    private int resultFromList(List<List<Integer>> hold){
        int res=0;
          for (int i = 0; i < hold.size(); i++) {
            String val= hold.get(i).stream().map(Object::toString).collect(Collectors.joining(""));
            res+=Integer.parseInt(val);
        }
        return res;
    }
     
    public List<List<Integer>> pathSum(TreeNode root) {
        if(root==null) return res;
        Stack<Integer> stk= new Stack<>();
        getPathSum(root,stk);

        return res;
    }
   private void  getPathSum(TreeNode root,Stack<Integer> stk){
        stk.push(root.val);
       if(root.left==null && root.right==null) {
           res.add(new ArrayList<>(stk));
           
        };
       if(root.left!=null)getPathSum(root.left,stk);
       if(root.right!=null)getPathSum(root.right,stk);
       stk.pop();
    }
}