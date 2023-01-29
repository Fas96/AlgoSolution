class LFUCache {
        final int capacity;
        int curSize;
        int minFrequency;
        Map<Integer, DLLNode> cache;
        Map<Integer, DLL> frequencyMap;


        public LFUCache(int capacity) {
            this.capacity = capacity;
            this.curSize = 0;
            this.minFrequency = 0;

            this.cache = new HashMap<>();
            this.frequencyMap = new HashMap<>();
        }
        public int get(int key) {
            DLLNode curNode = cache.get(key);
            if (curNode == null) {
                return -1;
            }
            updateNode(curNode);
            return curNode.value;
        }
        public void put(int key, int value) {

            if (capacity == 0) {
                return;
            }

            if (cache.containsKey(key)) {
                DLLNode curNode = cache.get(key);
                curNode.value = value;
                updateNode(curNode);
            } else {
                curSize++;
                if (curSize > capacity) {
                    
                    DLL minFreqList = frequencyMap.get(minFrequency);
                    cache.remove(minFreqList.tail.prev.key);
                    minFreqList.removeNode(minFreqList.tail.prev);
                    curSize--;
                }
                
                minFrequency = 1;
                DLLNode newNode = new DLLNode(key, value);

               
                DLL curList = frequencyMap.getOrDefault(1, new DLL());
                curList.addNode(newNode);
                frequencyMap.put(1, curList);
                cache.put(key, newNode);
            }
        }

        public void updateNode(DLLNode curNode) {
            int curFreq = curNode.freq;
            DLL curList = frequencyMap.get(curFreq);
            curList.removeNode(curNode);


            if (curFreq == minFrequency && curList.size == 0) {
                minFrequency++;
            }

            curNode.freq++;

            DLL newList = frequencyMap.getOrDefault(curNode.freq, new DLL());
            newList.addNode(curNode);
            frequencyMap.put(curNode.freq, newList);
        }
    }
   class DLLNode{
        int key;
        int value;
        int freq;
        DLLNode prev;
        DLLNode next;
        public DLLNode(int key, int value){
            this.key = key;
            this.value = value;
            this.freq = 1;
        }
   }
   class DLL{
        DLLNode head;
        DLLNode tail;
        int size;
        public DLL(){
            head = new DLLNode(-1, -1);
            tail = new DLLNode(-1, -1);
            head.next = tail;
            tail.prev = head;
            size = 0;
        }
        public void addNode(DLLNode node){
            node.next = head.next;
            node.prev = head;
            head.next.prev = node;
            head.next = node;
            size++;
        }
        public void removeNode(DLLNode node){
            node.prev.next = node.next;
            node.next.prev = node.prev;
            size--;
        }
        public DLLNode removeTail(){
            DLLNode node = tail.prev;
            removeNode(node);
            return node;
        }
   }