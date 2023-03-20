class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        if(n==0) return true;
        int N=flowerbed.length;
        for (int i = 0; i < N; i++) {
            if(flowerbed[i]==0){
                if(((i ==0 || flowerbed[i-1]==0)?0:1)==0 && ((i==flowerbed.length-1 || flowerbed[i+1]==0)?0:1)==0) {
                    flowerbed[i]=1;
                    n--;
                }
            }
            if(n==0) return true;
        }
        return false;
    }
}