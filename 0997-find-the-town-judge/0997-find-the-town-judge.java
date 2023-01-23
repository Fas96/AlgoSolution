class Solution {
    public int findJudge(int n, int[][] trust) {
         HashMap<Integer, List<Integer>> map = new HashMap<>();
        for (int[] t:trust) {
            List<Integer> list = map.getOrDefault(t[0], new ArrayList<>());
            list.add(t[1]);
            map.put(t[0], list);
        }

        for (int i = 1; i <= n; i++) {
            if (!map.containsKey(i)) {
                int count = 0;
                for (int j = 1; j <= n; j++) {
                    if (i == j) continue;
                    if (map.containsKey(j) && map.get(j).contains(i)) {
                        count++;
                    }
                }
                if (count == n - 1) return i;
            }
        }
        return -1; 
//          Set<Integer> trustiee = new HashSet<>();
//          Set<Integer> person = new HashSet<>();
//          for (int[] t : trust) {
//              trustiee.add(t[0]);
//              person.add(t[1]);
//          }

//         int judge = -1;
//         for (int p : person) {
//             if (!trustiee.contains(p)) {
//                 judge = p;
//                 break;
//             }
//         }

//         return judge;
    }
}