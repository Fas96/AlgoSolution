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
     public List<List<Integer>> verticalTraversal(TreeNode root) {
     Map<Integer,Map<Integer,List<Integer>>> res = new TreeMap<>();
    
    List<List<Integer>> ans= new ArrayList<>();
    
    int x=0,y=0;
    
    if(root==null) return ans;
    inOrderTraversal(root,res,x,y);
    
      for(Map<Integer, List<Integer>> maps : res.values()) {
            List<Integer> level = new ArrayList<>();
            for(List<Integer> list : maps.values()) {
                Collections.sort(list);
                level.addAll(list);  
            }
            ans.add(level);
        }

    return ans;
  }

  private void inOrderTraversal(TreeNode root,Map<Integer,Map<Integer,List<Integer>>> res,int x,int y) {
    if(root==null) return ;
 
    // res.computeIfAbsent(y, k -> new ArrayList<Integer>());
    // res.get(y).add(root.val );
    
      res.computeIfAbsent(y, key -> new TreeMap<>());
      res.get(y).computeIfAbsent(x, key -> new ArrayList<>());
      res.get(y).get(x).add(root.val);
    inOrderTraversal(root.left,res,x+1,y-1);
    // res.computeIfAbsent(y, k -> new ArrayList<Integer>());
    // res.get(y).add(root.val );
       System.out.println(x+"||"+y);
       // res.get(y).add(root.val );

      inOrderTraversal(root.right,res,x+1,y+1);
      
   
  }
}