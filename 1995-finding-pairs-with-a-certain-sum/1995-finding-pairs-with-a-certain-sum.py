class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.hm = defaultdict(set)
        for i,n in enumerate(nums2):
            self.hm[n].add(i)
        self.nums1 = nums1
        self.nums2 = nums2
        

    def add(self, index: int, val: int) -> None:
        ss = self.hm[self.nums2[index]]
        ss.remove(index)
        self.nums2[index]+=val
        self.hm[self.nums2[index]].add(index)
        

    def count(self, tot: int) -> int:
        ans = 0
        for k in self.nums1:
            target = tot-k
            ans+=len(self.hm[target])
        return ans
            
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)