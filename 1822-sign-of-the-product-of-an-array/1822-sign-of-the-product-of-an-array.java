import java.math.BigInteger;
class Solution {
    public int arraySign(int[] nums) {
         BigInteger ans= BigInteger.valueOf(1);
        for (int num : nums) {
            ans=ans.multiply(BigInteger.valueOf(num));
        }
        return ans.signum();
    }
}