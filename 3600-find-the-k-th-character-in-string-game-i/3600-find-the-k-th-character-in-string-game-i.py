class Solution:
    def kthCharacter(self, k: int) -> str:
        if k == 1:
            return 'a'
        pos = k - 1 
        increment = bin(pos).count('1')
        return chr(ord('a') + (increment % 26))