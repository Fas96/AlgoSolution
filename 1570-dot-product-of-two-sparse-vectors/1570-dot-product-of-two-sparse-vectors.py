class SparseVector:
    def __init__(self, nums: List[int]):
        self.mp = {i: x for i, x in enumerate(nums) if x}
        
    def dotProduct(self, vec: 'SparseVector') -> int:
        return sum(self.mp[key]*vec.mp.get(key, 0) for key in self.mp)
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)