class Solution {
    public int maxOperations(int[] nums, int k) {
    HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int res=0;
        for(int i:nums){
			int count = 0;
			if (map.containsKey(k - i)) {
				count = map.get(k - i);
				if (count > 0) {
					res++;
					map.put(k - i, --count);
				}
				else{
					map.put(i, map.getOrDefault(i,0)+1);
				}
			} else {
				map.put(i, map.getOrDefault(i,0)+1);
			}
        }
        return res;
                    
    }
}