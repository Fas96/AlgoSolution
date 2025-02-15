class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans=0
        def isSumofIntegersSubstringEqualsI(s, target, start=0, current_sum=0):
            if start == len(s):
                return current_sum == target
            for end in range(start + 1, len(s) + 1):
                num = int(s[start:end])
                if isSumofIntegersSubstringEqualsI(s, target, end, current_sum + num):
                    return True
            return False
        for i in range(1,n+1):
            if isSumofIntegersSubstringEqualsI(str(i*i), i):
                ans+=(i*i)
        return ans

        