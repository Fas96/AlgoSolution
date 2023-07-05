class Solution:
    def numDecodings(self, s: str) -> int:
        dfs = {}

        def helper(s):
            if s in dfs:
                return dfs[s]
            if not s:
                return 1
            if s[0] == '0':
                return 0
            if len(s) == 1:
                return 1
            res = helper(s[1:])
            if int(s[:2]) <= 26:
                res += helper(s[2:])
            dfs[s] = res
            return res

        return helper(s)
        