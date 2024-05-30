class Solution:
    def countTriplets(self, arr: List[int]) -> int: 
        return sum((j - i) for i in range(len(arr)) for j in range(i + 1, len(arr)) if not reduce(lambda x, y: x ^ y, arr[i:j + 1]))

        