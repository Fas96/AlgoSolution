class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def s(m):
            a=[]
            while m:
                a+=m.pop(0)
                if m and m[0]:
                    for r in m:
                        a.append(r.pop())
                if m:
                    a+=(m.pop()[::-1])
                if m and m[0]:
                    for r in m[::-1]:
                        a.append(r.pop(0))
            return a
        return s(matrix)



        