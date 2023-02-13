class Solution {
    public int balancedStringSplit(String s) {
         int ans = 0;
      
        int LCount=0, RCount=0;
        for(int i = 0; i < s.length(); i++) {
            if(s.charAt(i) == 'L') LCount++;
            else RCount++;
            if(LCount == RCount) {
                ans++;
                
            }
        }
        return ans;
    }
    
  
}

 