class Solution {
    public int[] twoSum(int[] numbers, int target) {
    int startInc=0,endDec=numbers.length-1;
    while (startInc<endDec) {
      if(numbers[startInc]+numbers[endDec]==target){
        return new int[]{startInc+1,endDec+1};
      } else if (numbers[startInc]+numbers[endDec]<target) {
        startInc++;
      } else if (numbers[startInc]+numbers[endDec]>target) {
        endDec--;
      }
    }
    return new int[]{-1,-1};  
    }
}