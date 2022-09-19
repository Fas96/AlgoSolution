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
    public TreeNode reverseOddLevels(TreeNode root) {
        
      Deque<TreeNode> queue=new LinkedList();
        int level = 0;
        int tmp;

        queue.add(root);
        while(!queue.isEmpty()) {
            int size = queue.size();
            if(level%2 == 1) {  // reversing the current level vals
                Deque<TreeNode> queue1 = new LinkedList(queue);
                while(!queue.isEmpty())
                {
                    tmp = queue.getFirst().val;
                    queue.getFirst().val = queue.getLast().val;
                    queue.getLast().val = tmp;
                    queue.pollFirst();
                    queue.pollLast();
                }
                queue=queue1;
            }

            if(queue.peek().left == null)     break;

            for(int i=0;i<size;i++) {
                TreeNode node = queue.poll();
                queue.add(node.left);
                queue.add(node.right);
            }
            level++;
        }
        return root;
    }
}