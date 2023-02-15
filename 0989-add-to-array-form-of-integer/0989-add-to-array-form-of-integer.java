import java.math.BigInteger;
class Solution {
    public List<Integer> addToArrayForm(int[] num, int k) {
          StringBuilder s = new StringBuilder();
        for (int i = 0; i < num.length; i++) {
            s.append(num[i]);
        }
        BigInteger n = new BigInteger(s.toString());
        BigInteger k1 = new BigInteger(String.valueOf(k));
        n = n.add(k1);
        String s1 = String.valueOf(n);
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < s1.length(); i++) {
            list.add(Integer.parseInt(String.valueOf(s1.charAt(i))));
        }
        return list;
    }
}