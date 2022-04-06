class Solution {
    public int climbStairs(int n) {
            if(n==0 || n==1) return 1;

        ArrayList<Integer> memo = new ArrayList<>();
        memo.add(1);
        memo.add(1);

        for (int i = 2; i < n+1; i++) {
            memo.add(memo.get(i-1)+ memo.get(i-2));
        } 
        return memo.get(n);
    }
}