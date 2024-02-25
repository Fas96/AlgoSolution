class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        p = self.parent.get(x, x)
        if p == x:
            return x
        self.parent[x] = self.find(p)
        return self.parent[x]

    def union(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)
        if randint(0, 1) > 0:
            self.parent[p_x] = p_y
        else:
            self.parent[p_y] = p_x

    def reset(self, x):
        self.parent[x] = x


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind()
        if len(nums) == 1:
            return True

        for num in nums:
            if num == 1:
                return False
            d = 2
            while d * d <= num:
                if num % d == 0:
                    uf.union(num, d)
                    uf.union(num, num / d)
                d += 1
        
        uniq = set()
        for num in nums:
            uniq.add(uf.find(num))
            if len(uniq) > 1:
                return False
        return True