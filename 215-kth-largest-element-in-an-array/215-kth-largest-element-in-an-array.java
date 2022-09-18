class Solution {
    public int findKthLargest(int[] nums, int k) {
            PriorityQueue<Integer> ans = new PriorityQueue<Integer>(k + 1);
    
                for(int el : nums) {
                    ans.add(el);
                    if (ans.size() > k) {
                        ans.poll();
                    }
                }

                return ans.poll();
    }
}