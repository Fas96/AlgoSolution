class Trie {
  
     TrieNode root = new TrieNode();
    public Trie() {
        
    }
    
    public void insert(String word) {
         TrieNode cur = root;
            for (int i = 0; i < word.length(); i++) {
                char c = word.charAt(i);
                int index = c - 'a';
                if (cur.nodes[index] == null) cur.nodes[index] = new TrieNode();
                cur = cur.nodes[index];
            }
            cur.isWord = true;
    }
    
    public boolean search(String word) {
         TrieNode cur = root;
            for (int i = 0; i < word.length(); i++) {
                char c = word.charAt(i);
                int index = c - 'a';
                if (cur.nodes[index] == null) return false;
                cur = cur.nodes[index];
            }
            return cur.isWord;
    }
    
    public boolean startsWith(String prefix) {
         TrieNode cur = root;
            for (int i = 0; i < prefix.length(); i++) {
                char c = prefix.charAt(i);
                int index = c - 'a';
                if (cur.nodes[index] == null) return false;
                cur = cur.nodes[index];
            }
            return true;
    }
    
    
    
     private class TrieNode {
            public boolean isWord = false;
            public TrieNode[] nodes = new TrieNode[26];
        }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */