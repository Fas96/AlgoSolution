class Solution {
    public boolean canMakeArithmeticProgression(int[] arr) {
         Arrays.sort(arr);
        int initialDiff=arr[1]-arr[0];
        for (int i = 1; i < arr.length; i++) {
           if(initialDiff != arr[i]-arr[i-1])return false;
        }
        return true;
    }
}