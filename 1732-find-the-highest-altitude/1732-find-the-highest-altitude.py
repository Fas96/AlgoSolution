class Solution:
    def largestAltitude(self, gain: List[int]) -> int: 
        cur , mhi = 0, 0
        for idx in gain:
            cur += idx
            mhi=max(mhi,cur) 
        return mhi
        