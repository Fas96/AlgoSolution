class Solution {
    public int findJudge(int n, int[][] trust) {
        if (n == 1) return 1;
        if (trust.length == 0) return -1;
        
        Set<Integer> trustiee = new HashSet<>();
        Set<Integer> person = new HashSet<>();
        for (int[] t : trust) {
            trustiee.add(t[0]);
            person.add(t[1]);
        }

        for (int p : person) {
            if (!trustiee.contains(p)) {
                int count = 0;
                //The town judge trusts nobody.
                for (int[] t : trust) {
                    if (t[1] == p) count++;
                }
                if (count == n - 1) return p;
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