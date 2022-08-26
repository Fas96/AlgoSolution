class Solution {
    public int[] twoSum(int[] numbers, int target) {
         int startInc=0,endDec=0;
    int N=numbers.length;
    for (int i = 0; i <N ; i++) {
      if(numbers[startInc]+numbers[N-1-endDec]==target){
       
        return new int[]{startInc+1,N-1-endDec+1};
      } else if (numbers[startInc]+numbers[N-1-endDec]<target) {
        startInc++;
      } else if (numbers[startInc]+numbers[N-1-endDec]>target) {
        endDec++;
      }
    }
    return new int[]{};  
    }
}