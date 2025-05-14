class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        m = (10 ** 9) + 7
        p = 1
        temp = [[0 for _ in range(26)] for _ in range(26)]
        hold = copy.deepcopy(temp)
        ch = 97
        for i, j in enumerate(nums):
            for k in range(ch + 1, ch + j + 1):
                val = k - 97
                val %= 26
                hold[i][val] += 1
            ch += 1
        
        def rec(t):
            if t == 1:
                return hold
            n = 1
            prev = copy.deepcopy(hold)
            while n * 2 <= t:
                cur = copy.deepcopy(temp)
                for i in range(97, 123):
                    val = i - 97
                    for j, k in enumerate(prev[val]):
                        if k > 0:
                            for x, y in enumerate(prev[j]):
                                cur[val][x] = (cur[val][x] + (y * k)) % m
                n *= 2
                prev = copy.deepcopy(cur)
            if n == t:return cur
            more = t - n
            more = rec(more)
            ans = copy.deepcopy(temp)
            for i in range(97, 123):
                val = i - 97
                for j, k in enumerate(cur[val]):
                    if k > 0:
                        for x, y in enumerate(more[j]):
                            ans[val][x] = (ans[val][x] + (y * k)) % m
            return ans
        
    
        helper = rec(t)
        ans = 0
        c = Counter(s)
        for i, j in c.items():
            ans = (ans + (sum(helper[ord(i) - 97]) * j)) % m
        return ans



        