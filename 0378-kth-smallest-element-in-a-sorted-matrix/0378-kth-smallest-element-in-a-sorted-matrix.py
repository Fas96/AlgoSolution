class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr= reduce(lambda x,y :x+y ,matrix)
        arr.sort() 
        return arr[k-1]
        