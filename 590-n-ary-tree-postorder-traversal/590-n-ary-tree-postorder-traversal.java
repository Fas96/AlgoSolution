/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
 
    List<Integer> list = new ArrayList<Integer>();
    public List<Integer> postorder(Node root) {
        
    Stack<Node> st = new Stack<Node>(); 
    
    if(root == null) return list;
    
    st.push(root);
    
    while(!st.isEmpty()){
        
        Node n = st.pop();    
        list.add(0, n.val);
        
        for(int i = 0; i < n.children.size(); i++ ){
            st.push(n.children.get(i));   // add all the children to stack and repeat the process
        }
        
    }
            
    return list;
    }
}