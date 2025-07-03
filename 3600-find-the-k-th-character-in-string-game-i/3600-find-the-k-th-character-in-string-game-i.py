class Solution:
    def kthCharacter(self, k: int) -> str:
        if k == 1: return 'a' 
        return chr(ord('a') + (( bin(k - 1).count('1')) % 26))