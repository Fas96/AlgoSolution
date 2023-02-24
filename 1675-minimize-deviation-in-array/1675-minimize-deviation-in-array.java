class Solution {
    public int minimumDeviation(int[] nums) {
        TreeSet<Integer> incDev = new TreeSet<>();
        
        for (int num : nums) incDev.add(num % 2 == 0 ? num : num * 2);
        
        int minDev = incDev.last() - incDev.first();
        
        while (incDev.last() % 2 == 0) {
            incDev.add(incDev.pollLast() / 2);
            minDev = Math.min(minDev, incDev.last() - incDev.first());
        }
        
        return minDev;
    }
}