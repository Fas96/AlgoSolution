class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        data = set()
        half = (n+1) // 2
        start = 10 ** (half - 1)
        end = 10 ** half

        for h in range(start, end):
            h = str(h)
            if n%2 == 1:
                s = h + h[:-1][::-1] 
            else:
                s = h + h[::-1] 
            
            if int(s) % k == 0:
                data.add("".join(sorted(s)))
        
        fact = [1] * (n+1)
        for i in range(1, n+1):
            fact[i] = fact[i-1] * i

        total = 0
        for s in data:
            count = [0]*10
            for ch in s:
                count[int(ch)] += 1

            perms = 0
            for d in range(1, 10):
                if count[d] == 0:
                    continue
                count[d]-=1
                p = fact[n-1]
                for c in count:
                    p = p // fact[c]
                perms = perms + p
                count[d]+=1
            total = total + perms
        return total