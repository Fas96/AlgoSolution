import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import java.util.Optional;
class Solution {
 public int characterReplacement(String s, int k) {
        int mx=0,N=s.length(),L=0,R=0,counter=0;
        Map<Character,Integer> hm= new HashMap<>();
        char[] sArr=s.toCharArray();
        int maxFreHm=0;
        while (R<N){
            hm.merge(sArr[R],1,Integer::sum);
             maxFreHm=maxUsingStreamAndMethodReference(hm);

            if ( (R-L+1)-maxFreHm>k) {
                hm.merge(sArr[L],-1,Integer::sum);
                L++;
            }
            mx=Math.max(mx,R-L+1);
            R++;
        }

        return  mx;

    }
    private <K, V extends Comparable<V>> V maxUsingStreamAndMethodReference(Map<K, V> map) {
        Optional<Map.Entry<K, V>> maxEntry = map.entrySet()
                .stream()
                .max(Comparator.comparing(Map.Entry::getValue));
        return maxEntry.get()
                .getValue();
    }
}