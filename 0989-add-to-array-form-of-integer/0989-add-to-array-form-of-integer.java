import java.math.BigInteger;
class Solution {
    public List<Integer> addToArrayForm(int[] num, int k) {
        StringBuilder s = new StringBuilder();
 
        for (int i : num) s.append(i);
        
        BigInteger n = (new BigInteger(s.toString())).add(new BigInteger(String.valueOf(k)));
        
        String s1 = String.valueOf(n);
 
       return s1.chars().mapToObj(c -> c - '0').collect(Collectors.toList());
 
    }
}