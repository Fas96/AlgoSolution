class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        ar=list(map(int,nums))
        ar.sort()
        return str(ar[-k])