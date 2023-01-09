class Solution {
    public long maxKelements(int[] nums, int k) { 
   long ans= 0; 
        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
        for(int i = 0; i < nums.length; i++){
            pq.add(nums[i]);
        }
        while (k > 0 && !pq.isEmpty()){
            int cur = pq.poll();
            ans += cur;
            pq.add((cur+2)/3);
            k--;
        }

        return ans;
    }

    private int bSearch(int[] nums) {
        int max = Integer.MIN_VALUE;
        int index = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > max) {
                max = nums[i];
                index = i;
            }
        }
        return index;
    }
 

    private int ceilF(int num) {
         return (int) Math.ceil((double) num / 3);
    }
}