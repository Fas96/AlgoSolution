class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total_xor = 0
        for num in nums: total_xor ^= num
        
        target_xor = total_xor ^ k
        
        # Count the number of set bits in target_xor
       
        return bin(target_xor).count('1')
        