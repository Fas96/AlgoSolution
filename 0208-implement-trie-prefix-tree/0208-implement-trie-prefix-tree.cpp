class Trie {
    struct TrieNode{
        char val;
        int count;
        int endsHere;
        TrieNode *child[26];
    };
    TrieNode *root;
    TrieNode *getNode(int index){
        TrieNode *newNode=new TrieNode;
        newNode->val='a'+index;
        newNode->count=newNode->endsHere=0;
        for(int i=0;i<26;++i){
            newNode->child[i]=NULL;
        }
        return newNode;
    }
public:
    Trie() {
        root=getNode('/'-'a');
    }
    
    void insert(string word) {
        TrieNode *curr=root;
        int index;
        for(int i=0; word[i]!='\0';++i){
            index=word[i]-'a';
            if(curr->child[index]==NULL){
                curr->child[index]=getNode(index);
            }
            curr->child[index]->count+=1;
            curr=curr->child[index];
        }
        curr->endsHere+=1;
        
    }
    
    bool search(string word) {
        TrieNode *curr=root;
        int index;
        for(int i=0; word[i]!='\0';++i){
             index=word[i]-'a';
              if(curr->child[index]==NULL){
               return false;
            } 
            curr=curr->child[index];
        }
        return (curr->endsHere>0);
    }
    
    bool startsWith(string prefix) {
        TrieNode *curr=root;
        int index;
        for(int i=0; prefix[i]!='\0';++i){
             index=prefix[i]-'a';
              if(curr->child[index]==NULL){
               return false;
            } 
            curr=curr->child[index];
        }
        return (curr->count>0);
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */