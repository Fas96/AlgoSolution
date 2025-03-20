class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def spiral(m):
            ans=[]
            while m:
                ans+=m.pop(0)

                if m and m[0]:
                    for r in m:
                        ans.append(r.pop())
                if m:
                    ans+=(m.pop()[::-1])
                if m and m[0]:
                    for r in m[::-1]:
                        ans.append(r.pop(0))
            return ans
        return spiral(matrix)


        