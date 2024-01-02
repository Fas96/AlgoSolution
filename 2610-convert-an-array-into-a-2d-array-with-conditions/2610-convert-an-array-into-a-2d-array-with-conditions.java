class Solution {
    public List<List<Integer>> findMatrix(int[] nums) {
         List<List<Integer>> output = new ArrayList<>();
        List<Integer> inputList = new ArrayList<>();
        
        for (int num : nums)inputList.add(num);
        

        while (!inputList.isEmpty()) {
            Set<Integer> uniqueSet = new HashSet<>(inputList);
            List<Integer> uniqueList = new ArrayList<>(uniqueSet);
            output.add(uniqueList);

            for (Integer i : uniqueList) {
                inputList.remove(i);
            }
        }

        return output;
        
    }
}