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
    public int pathSum(TreeNode root, int targetSum) { 
        Map<Long, Integer> mapPrefixSum = new HashMap<>();
        mapPrefixSum.put(0L, 1);
        return prefixSum(root, targetSum, 0, mapPrefixSum);
    }

    private int prefixSum(TreeNode root, int targetSum, long currSum, Map<Long,Integer> mapPrefixSum) {
        if(root == null)
            return 0;
        currSum += root.val ;
        int count = 0;
        if(mapPrefixSum.containsKey(currSum-targetSum)){
            count += mapPrefixSum.get(currSum-targetSum);
        }
         
        mapPrefixSum.merge(currSum, 1, Integer::sum);
        int left = prefixSum(root.left,targetSum,currSum,mapPrefixSum) ;
        int right = prefixSum(root.right,targetSum,currSum,mapPrefixSum);
        
        mapPrefixSum.merge(currSum, -1, Integer::sum);

        return count+left+right;
    }

}