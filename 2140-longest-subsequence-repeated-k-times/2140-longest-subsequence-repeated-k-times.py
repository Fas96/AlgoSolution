class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:

        count = Counter(s)
        words = [c for c in count.keys() if count[c]>=k]
        words.sort()
        q = deque([''])
        def check(s,t): 
            t = iter(t)
            return all(c in t for c in s)
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                res = cur
                for c in words:
                    next = cur+c 
                    if check(next*k,s):
                        q.append(next)
        return res 