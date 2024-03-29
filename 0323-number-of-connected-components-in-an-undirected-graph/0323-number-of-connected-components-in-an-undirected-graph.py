class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        class DisjointSet:
            def __init__(self, n):
                self.data = [-1 for _ in range(n)]
                self.size = n

            def upward(self, change_list, index):
                value = self.data[index]
                if value < 0:
                    return index

                change_list.append(index)
                return self.upward(change_list, value)

            def find(self, index):
                change_list = []
                result = self.upward(change_list, index)

                for i in change_list:
                    self.data[i] = result

                return result

            def union(self, x, y):
                x = self.find(x)
                y = self.find(y)

                if x == y:
                    return

                if self.data[x] < self.data[y]:
                    self.data[y] = x
                elif self.data[x] > self.data[y]:
                    self.data[x] = y
                else:
                    self.data[x] -= 1
                    self.data[y] = x

                self.size -= 1
        uf =DisjointSet(n) 
        for u,v in edges:
            uf.union(u,v)
        return uf.size
        