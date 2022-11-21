class Solution {
    public boolean canJump(int[] A) {
            int furthestReachSoFar = 0, lastIdx = A.length - 1;
        for (int i = 0; i <= furthestReachSoFar && furthestReachSoFar < lastIdx; ++i) {
            furthestReachSoFar = Math.max(furthestReachSoFar, A[i] + i);
        } 

        return furthestReachSoFar >= lastIdx;
    }
    
    
}
