class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return list(set(edges[1]) & set(edges[0]))[0]
        