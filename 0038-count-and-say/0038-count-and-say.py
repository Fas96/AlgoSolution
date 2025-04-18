class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"
        def formRLE(rle):
            res,i,n = [],0, len(rle)
            while i < n:
                curCH,cnt = rle[i],1 
                while i + 1 < n and rle[i+1] == curCH:
                    i += 1
                    cnt += 1
                res.append(f"{cnt}{curCH}")
                i += 1
            return "".join(res)

        for _ in range(n-1):
            ans = formRLE(ans)
        return ans
        