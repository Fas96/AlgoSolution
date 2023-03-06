import java.math.BigInteger;
class Solution {
     public int findValidSplit(int[] nums) {
//         int n = nums.length;
//         BigInteger[] prefixProd = new BigInteger[n];
//         BigInteger[] suffixProd = new BigInteger[n];
//         prefixProd[0] = BigInteger.valueOf(nums[0]);
//         suffixProd[n-1] = BigInteger.valueOf(nums[n-1]);
//         for (int i = 1; i < n; i++) { 
//             prefixProd[i] = prefixProd[i-1].multiply(BigInteger.valueOf(nums[i])); 
//             suffixProd[n-i-1] = suffixProd[n-i].multiply(BigInteger.valueOf(nums[n-i-1]));
//         }

//         for (int i = 0; i < n-1; i++) {
//             if (gcd(prefixProd[i], suffixProd[i+1]).equals(BigInteger.ONE)) {
//                 return i;
//             }
//         }

//         return -1;
          int possible =0;
        int n = nums.length;
        for(int i=0;i<=possible;i++){
            int ele = nums[i];
            for(int j=i+1;j<n;j++){
                if(nums[j]%ele==0) possible = Math.max(possible,j);
                if(ele%nums[j]==0) possible = Math.max(possible,j);
            }
        }
        return possible<=(n-2)?possible:-1;
    }

    // private BigInteger gcd(BigInteger a, BigInteger b) {
    //     return a.gcd(b);
    // }
}