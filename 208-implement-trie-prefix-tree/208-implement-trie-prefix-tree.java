class Trie {

    private TrieNode root;
    public Trie() {
        root=new TrieNode();
        
    }
    
    public void insert(String word) {
        TrieNode curNode=root;
        char[] arr=word.toCharArray();
        for(char curChar:arr){
            if(!curNode.children.containsKey(curChar)){
                curNode.children.put(curChar,new TrieNode());
            }
            curNode=curNode.children.get(curChar);
        }
        curNode.isWord=true;
    }
    
    public boolean search(String word) {
        TrieNode curNode=root;
        char[] arr=word.toCharArray();
        for(char curChar:arr){
            if(!curNode.children.containsKey(curChar)){
                return false;
            }
            curNode=curNode.children.get(curChar);
        }
        return curNode.isWord;
    }
    
    public boolean startsWith(String prefix) {
           TrieNode curNode=root;
        char[] arr=prefix.toCharArray();
        for(char curChar:arr){
            if(!curNode.children.containsKey(curChar)){
                return false;
            }
            curNode=curNode.children.get(curChar);
        }
        return true;
    }
}

class TrieNode{
    Map<Character,TrieNode> children=new HashMap<>();
    boolean isWord=false;
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */