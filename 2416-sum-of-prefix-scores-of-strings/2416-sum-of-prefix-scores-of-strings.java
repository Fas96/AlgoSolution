class Solution {
      final int m = 1023;
    public int[] sumPrefixScores(String[] words) {
//         int N=words.length;
 
//         int[] res= new int[N];
//         Map<String,Integer> hm= new HashMap<>();
//         for (int i = 0; i < N; i++) {
//             for (int j = 0; j <words[i].length(); j++) {
//                 hm.merge(words[i].substring(0,j+1),1,Integer::sum);
//             }
//         }
//         for (int i = 0; i < N; i++) {
//             int sum=0;
//             for (int j = 0; j < words[i].length(); j++) {
//                sum+= hm.getOrDefault(words[i].substring(0,j+1),0);
//             }
//            res[i]=sum;
//         }

//         return res;
        HashMap<Long,Integer> map = new HashMap<>();
        for(String S : words)
        {
            char[] s = S.toCharArray();
            long hash_so_far = 0L;
            int n = s.length;
            for (int i = 0; i < n; i++)
            {
                hash_so_far = hash_so_far*m+s[i];
                map.put(hash_so_far,map.getOrDefault(hash_so_far,0)+1);
            }
        }
        int cur = 0;
        int[] ret = new int[words.length];
        for(String S : words)
        {
            char[] s = S.toCharArray();
            long hash_so_far = 0L;
            int n = s.length;
            for (int i = 0; i < n; i++)
            {
                hash_so_far = hash_so_far*m+s[i];
                ret[cur] += map.get(hash_so_far);
            }
            cur++;
        }
        return ret;
    }
}