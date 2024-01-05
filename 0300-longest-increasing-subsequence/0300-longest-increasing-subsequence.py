class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return len(reduce(lambda l,q:l[:(i:=bisect_left(l,q))]+[q]+l[i+1:],nums,[]))
        