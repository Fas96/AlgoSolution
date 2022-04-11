class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        List<List<Integer>> res= new ArrayList<>();
        List<Integer> one= new ArrayList<>();
        List<Integer> two= new ArrayList<>();
        for (int n : nums1) {
            if(!Arrays.stream(nums2).anyMatch(e->e==n)){
               
                if(!one.contains(n)) one.add(n);
            };
        }
        for (int n : nums2) {
            if(!Arrays.stream(nums1).anyMatch(e->e==n)){
                if(!two.contains(n)) two.add(n);
            };
        }
        res.add(one);
        res.add(two);
        return res;
    }
}