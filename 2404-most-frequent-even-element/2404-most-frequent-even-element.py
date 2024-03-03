class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq=Counter(nums)
        nums=sorted(nums)
        mx=-1
        xx=-127263
        for x in nums:
            if freq[x]>mx and x%2==0:
                mx=freq[x]
                xx=x

        return -1 if mx==-1 else xx
        