/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    private HashMap<Integer, Node> seen = new HashMap<>();
    public Node cloneGraph(Node node) {
        if(node==null) return node;
        int id = node.val;
        Node curNode = null;
        if (!seen.containsKey(id)) {
            curNode = new Node(id, new ArrayList<>());
            seen.put(id, curNode);
            for (Node child : node.neighbors) {
                int childId = child.val;
                if (seen.containsKey(childId)) {
                    Node newChild = seen.get(childId);
                    curNode.neighbors.add(newChild);
                } else {
                    Node newChild = cloneGraph(child);
                    curNode.neighbors.add(newChild);
                }
            }
        }
        return curNode;
    }
}