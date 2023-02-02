class Solution {
    public boolean isAlienSorted(String[] words, String order) {
         int n = words.length; 
        List<Character> orderList = order.chars().mapToObj(c -> (char) c).collect(Collectors.toList());
        for (int i = 0; i < n-1; i++) {
            if(!isAlienSorted(words[i], words[i+1], orderList,words[i].length(),words[i+1].length())) return false;
        }
        return true;
    }
    
    private boolean isAlienSorted(String word1, String word2, List<Character> orderList,int n,int m) {
     
        for (int i = 0;i < n && i < m;i++){
            if(word1.charAt(i) != word2.charAt(i)) {
                return orderList.indexOf(word1.charAt(i)) < orderList.indexOf(word2.charAt(i));
            }
        }
        return n <= m;
    }
    
}