class Solution {
    public int minimumRounds(int[] tasks) {
         HashMap<Integer, Integer> map = new HashMap<>();
        for (int task : tasks) {
            map.merge(task, 1, Integer::sum);
        }
        int minimumRounds = 0;
        for (int task : map.keySet()) {
            int numTasks = map.get(task);
            if(numTasks==1)return -1;
            minimumRounds += (numTasks / 3);
            if (numTasks % 3 != 0) {
                minimumRounds++;
            }
        }
        return minimumRounds;

    }
}