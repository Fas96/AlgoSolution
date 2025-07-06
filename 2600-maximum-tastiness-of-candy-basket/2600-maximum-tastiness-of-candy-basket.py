class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        if len(set(price))==1 or k==0:
            return 0
        price.sort()
        n=len(price)
        def isValid(num): 
            cnt = 1
            diff = price[0] + num
            for i in range(1,n):
                if price[i] >= diff:
                    diff = price[i] + num
                    cnt += 1 
            return cnt>= k
        low,high = 0,max(price) - min(price)
        ans = -1
        while low <= high:
            mid = (low + high) >> 1
            if isValid(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
        