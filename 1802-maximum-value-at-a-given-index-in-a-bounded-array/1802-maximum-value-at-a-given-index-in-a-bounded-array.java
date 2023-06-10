class Solution {
  public int maxValue(int n, int index, int maxSum) {
        long low = 1, high = maxSum, mid = 0, res = 0;
        long left = index + 1;
        long right = n - index - 1;

        while(low <= high){
            mid = low + (high-low)/2;
            if(isCondition(mid, left, right, maxSum)){
                res = mid;
                low = mid + 1;
            }else{
                high = mid - 1;
            }
        }
        return (int) res;
    }
    public boolean isCondition(long mid, long left, long right, int maxSum){
        long leftSum = 0, rightSum = 0;
        leftSum= (left < mid)? (left * mid - (left * (left - 1)/ 2)): ((mid * (mid + 1) / 2) + (left - mid));
        rightSum= (right < mid)? (right * mid - (right * (right + 1) / 2)): ( (mid * (mid - 1) / 2) + (right - mid + 1));
        return (leftSum + rightSum) <= maxSum;
    }
}