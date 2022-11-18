class Solution {
    public boolean isUgly(int n) {
        if(n==0) return false;
        while(true){
            if(n%2==0){
                n/=2;
                continue;
            }else if(n%3==0){
                n/=3;
                continue;
            }else if(n%5==0){
                n/=5;
                continue;
            }
            break;
        }
        
        return n==1;
    }
}