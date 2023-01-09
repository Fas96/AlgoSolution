class Solution {
    public long maxKelements(int[] nums, int k) { 
       
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int i = 0; i < nums.length; i++){
            pq.add(-nums[i]);
        }
        long ans= 0;
        while (k > 0 ){
            int cur = -pq.poll();
            ans += cur;
            cur = (cur+2)/3;
            pq.add(-cur);
            k--;
        }
         
        return ans;
//        int n = nums.length;
//        int maxKScore = 0;
//        int count = 0;
//
//
//        for (int i = 0; i < n; i++) {
//           int index=  binarySearchMaxIndex(nums);
//            maxKScore += nums[index];
//            System.out.println(Arrays.toString(nums));
//            System.out.println("maxKScore = " + maxKScore+" index = "+index);
//           nums[index] = ceilF(nums[index]);
//              count++;
//              if (count == k) break;
//        }
//        return maxKScore;
    }

    private int binarySearchMaxIndex(int[] nums) {
        int n = nums.length;
        int l = 0;
        int r = n - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] < nums[mid + 1]) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return l;
    }


    private int ceilF(int num) {
     return (int) Math.ceil((double) num / 3);
    }
}