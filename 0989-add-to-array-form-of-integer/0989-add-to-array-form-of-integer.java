import java.math.BigInteger;
class Solution {
    public List<Integer> addToArrayForm(int[] num, int k) {
        StringBuilder s = new StringBuilder();
 
        for (int i : num) s.append(i);
        
 
       return  String.valueOf((new BigInteger(s.toString())).add(new BigInteger(String.valueOf(k)))).chars().mapToObj(c -> c - '0').collect(Collectors.toList());
 
    }
}