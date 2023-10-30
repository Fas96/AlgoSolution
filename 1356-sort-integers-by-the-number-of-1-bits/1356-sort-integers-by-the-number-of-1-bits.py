class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        n=[]
        for i in arr:
             n.append([i,(bin(i)[2:]).count('1')])
        print(n)
        n=sorted(n, key=lambda x: (x[1], x[0]))
        print(n)
        return [x[0] for x in n]
        