// class Node {
//     public int val;
//     public int key;
//     public Node next;

//     public Node() {
//     }
// }
class MyHashMap {
    
    
   int[] map;
    int size = 1;
    public MyHashMap() {
        map = new int[size];
        Arrays.fill(map, -1);
    }
    
    public void put(int key, int value) {
        if (key >= size) {
            int[] newMap = new int[key + size + 1];
            Arrays.fill(newMap, -1);
            System.arraycopy(map, 0, newMap, 0, size);
            size = newMap.length;
            map = newMap;
        }
        map[key] = value;
    }
    
    public int get(int key) {
        if (key >= size) return -1;
        return map[key];
    }
    
    public void remove(int key) {
        if (key >= size) return;
        map[key] = -1;
    }


//      private static final int size = 10000;
    
//     Node[] hashSet = new Node[size];
    
//     public MyHashMap() {

//     }

//     public void put(int key,int val) {
//         Node pointer = hashSet[key % size];
//         if (pointer == null) {
//             hashSet[key % size] = new Node(key);
//         } else {
//             Node current = pointer;
//             Node previous = current;
//             while (current != null) {
//                 if (current.val == key) return;
//                 previous = current;
//                 current = current.next;
//             }
//             previous.next = new Node(key);
//         }

//     }

//     public void remove(int key) {

//         Node current = hashSet[key % size];

//         while (current != null) {
//             if (current.val == key) {
//                 current.val = -1; // Simply replace with -1
//                 return;
//             }
//             current = current.next;
//         }
//     }

//     public void get(int key) {
//         Node current = hashSet[key % size];
//         while (current != null) {
//             if (current.key == key) return current.val;
//             current = current.next;
//         }
//         return false;
//     }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */