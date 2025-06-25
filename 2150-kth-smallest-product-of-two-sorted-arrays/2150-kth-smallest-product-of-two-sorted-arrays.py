class Solution:
    def kthSmallestProduct(self, A: List[int], B: List[int], k: int) -> int:
        A.sort(); B.sort()
        def count(x):
            total = 0
            for a in A:
                if a > 0:
                    # For positive a, count elements in B where b <= x//a
                    count = bisect_right(B, x // a)
                elif a < 0:
                    # For negative a, count elements in B where b >= ceil(x/a)
                    # (since multiplying by negative reverses inequality)
                    count = len(B) - bisect_left(B, math.ceil(x / a))
                else:  # a == 0
                    # If a is zero, then a*b = 0 for all b
                    # So count all elements in B if x >= 0, else 0
                    count = len(B) if x >= 0 else 0
                total += count
            return total
         
        l, r = -10**10, 10**10
        while l < r:
            m = (l + r) // 2
            if count(m)<k:l=m+1
            else: r=m
        return l

        

       
                    

        