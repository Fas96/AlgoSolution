class Solution {
    public int totalFruit(int[] fruits) {
       HashMap<Integer, Integer> map = new HashMap<>();
        int max = 0;
        int start = 0;
        for (int i = 0; i < fruits.length; i++) {
            map.merge(fruits[i], 1, Integer::sum);
            while (map.size() > 2) {
                int count = map.get(fruits[start]);
                if (count == 1) {
                    map.remove(fruits[start]);
                } else {
                    map.put(fruits[start], count - 1);
                }
                start++;
            }
            max = Math.max(max, i - start + 1);
        }


        return max;
    } 
}