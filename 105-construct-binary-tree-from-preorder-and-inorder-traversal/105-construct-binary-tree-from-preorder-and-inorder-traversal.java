class Solution {   
    int[] preorder;
    int[] inorder;
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        this.preorder = preorder;
        this.inorder = inorder;
        return helper(0, 0, inorder.length-1);
    }
    
    public TreeNode helper(int pre_start, int in_start, int in_end){
        if (in_start > in_end || pre_start>=preorder.length){
            return null;
        }
        int cur = preorder[pre_start];
        int cur_index = 0;
        for (int i = in_start; i <= in_end; i++){
            if (inorder[i] == cur){
                cur_index = i;
                break;
            }
        }
        TreeNode root = new TreeNode(cur);
        root.left = helper(pre_start+1, in_start, cur_index-1);
        root.right = helper(pre_start+cur_index-in_start+1, cur_index+1, in_end);
        
        return root;
        
    }
}