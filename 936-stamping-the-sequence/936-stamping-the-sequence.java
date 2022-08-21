class Solution {
    //cp
//   public int[] movesToStamp(String stamp, String target) {
//         char[] S = stamp.toCharArray();
//         char[] T = target.toCharArray();
//         List<Integer> res = new ArrayList<>();
//         boolean[] visited = new boolean[T.length];
//         int stars = 0;
        
//         while (stars < T.length) {
//             boolean doneReplace = false;
//             for (int i = 0; i <= T.length - S.length; i++) {
//                 if (!visited[i] && canReplace(T, i, S)) {
//                     stars = doReplace(T, i, S.length, stars);
//                     doneReplace = true;
//                     visited[i] = true;
//                     res.add(i);
//                     if (stars == T.length) {
//                         break;
//                     }
//                 }
//             }
            
//             if (!doneReplace) {
//                 return new int[0];
//             }
//         }
        
//         int[] resArray = new int[res.size()];
//         for (int i = 0; i < res.size(); i++) {
//             resArray[i] = res.get(res.size() - i - 1);
//         }
//         return resArray;
//     }
    
//     private boolean canReplace(char[] T, int p, char[] S) {
//         for (int i = 0; i < S.length; i++) {
//             if (T[i + p] != '*' && T[i + p] != S[i]) {
//                 return false;
//             }
//         }
//         return true;
//     }
    
//     private int doReplace(char[] T, int p, int len, int count) {
//         for (int i = 0; i < len; i++) {
//             if (T[i + p] != '*') {
//                 T[i + p] = '*';
//                 count++;
//             }
//         }
//         return count;
//     } 
      public int[] movesToStamp(String stamp, String target) {
        LinkedList<Integer> ans = new LinkedList<>();
        char[] T = target.toCharArray(), S = stamp.toCharArray();
        int sz, m = stamp.length(), n = target.length(), del = 0;
        do{ sz = ans.size();
            for (int i = 0; i < n - m + 1; i++){
                boolean ok = T[i] != 'X'; // ok to stamp?
                for (int j = i; j < i + m && ok; j++){
                    ok &= T[j] == 'X' || T[j] == '?' || T[j] == S[j - i]; // all these conds must be met for stamp length
                }
                for (int j = i; j < i + m && ok; j++){
                    if (Character.isLowerCase(T[j])){ // delete a letter
                        del++;
                    }
                    T[j] = j == i || T[j] == 'X'? 'X' : '?'; // mark 'X' and '?' accordingly
                }
                if (ok){
                    ans.addFirst(i);
                }
            }
        }while(sz != ans.size() && del != n);

        return del != n? new int[0] : ans.stream().mapToInt(o -> o).toArray();
    }
}