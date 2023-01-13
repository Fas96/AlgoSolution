class Solution {
   class TreeNode {
        char val;
        List<TreeNode> children;
        public TreeNode(char val){
            this.val = val;
            this.children = new ArrayList<>();
        }
    }
    private int max;
    public int longestPath(int[] parent, String s) {
        TreeNode root = buildTree(parent, s);
        backtrack(root);
        return max;
    }
    private TreeNode buildTree(int[] parent, String s){
        Map<Integer, TreeNode> pMap = new HashMap<>();
        for(int i=0;i<s.length();i++){
            pMap.put(i, new TreeNode(s.charAt(i)));
        }
        for(int i=1;i<s.length();i++){
            pMap.get(parent[i]).children.add(pMap.get(i));
        }
        return pMap.get(0);
    }
    private int backtrack(TreeNode root){
        int max1 = 0;
        int max2 = 0;
        for(TreeNode child : root.children){
            int childLengh = backtrack(child);
            if(child.val != root.val){
                if(childLengh > max1){
                    max2 = max1;
                    max1 = childLengh;
                } else if(childLengh > max2){
                    max2 = childLengh;
                }
            }
        }

        max = Math.max(max, max1 + max2 + 1);
        return Math.max(max1, max2) + 1;
    }
}