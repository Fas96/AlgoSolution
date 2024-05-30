class Solution:
    def countTriplets(self, arr: List[int]) -> int: 
        n=len(arr)
        return sum((j - i) for i in range(n) for j in range(i + 1, n) if not reduce(lambda x, y: x ^ y, arr[i:j + 1]))

        