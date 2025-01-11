class Solution {
public:
    int hammingWeight(int n) {
     
        int ans; 
            while(n != 0){
                if(n&1)ans+=1;
                n= n>>1;
            } 
        
        return ans;
 
    }
};