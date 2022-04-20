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
class BSTIterator {
     Queue<Integer> treelist=new LinkedList<>();
    public BSTIterator(TreeNode root) {
        inorder(root);
    }
    public void inorder(TreeNode root){
        if(root==null)
            return;
        inorder(root.left);
        treelist.add(root.val);
        inorder(root.right);
    }
    public int next() {
        return treelist.poll();
    }
    
    public boolean hasNext() {
        return !treelist.isEmpty();
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */