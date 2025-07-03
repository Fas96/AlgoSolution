class Solution:
    def kthCharacter(self, k: int) -> str:
        if k == 1: return 'a' 
        increment = bin(k - 1).count('1')
        return chr(ord('a') + (increment % 26))