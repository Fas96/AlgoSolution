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
    public List<List<Integer>> levelOrder(Node root) {
        
      List<List<Integer>> levelList = new ArrayList<>(); 
    if (root == null)return levelList;
    
    Queue<Node> main_queue = new LinkedList<>();
  
    main_queue.offer(root); 
    while (!main_queue.isEmpty()) {
      
      List<Integer> temp = new ArrayList<>();
      int size = main_queue.size();
      // Iterate through the current level
      for (int i = 0; i < size; i++) {
        Node node = main_queue.poll();
        temp.add(node.val);
 
        for (Node child : node.children) {
          main_queue.offer(child);
        }
      }
 
      levelList.add(temp);
        
        
    }
     
      
    return levelList;
    }
    
}