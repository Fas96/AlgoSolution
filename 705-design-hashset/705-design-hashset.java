class Node {
    public int val;
    public Node next;

    public Node(int val) {
        this.val = val;
    }
}

class MyHashSet {

    private static final int size = 10000;
    
    Node[] hashSet = new Node[size];
    
    public MyHashSet() {

    }

    public void add(int key) {
        Node pointer = hashSet[key % size];
        if (pointer == null) {
            hashSet[key % size] = new Node(key);
        } else {
            Node current = pointer;
            Node previous = current;
            while (current != null) {
                if (current.val == key) return;
                previous = current;
                current = current.next;
            }
            previous.next = new Node(key);
        }

    }

    public void remove(int key) {

        Node current = hashSet[key % size];

        while (current != null) {
            if (current.val == key) {
                current.val = -1; // Simply replace with -1
                return;
            }
            current = current.next;
        }
    }

    public boolean contains(int key) {
        Node current = hashSet[key % size];
        while (current != null) {
            if (current.val == key) return true;
            current = current.next;
        }
        return false;
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */