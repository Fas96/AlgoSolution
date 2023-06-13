class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        letters = "abcdefghijklmnopqrstuvwxyz"
        for letter in letters:
            if s.count(letter) != t.count(letter):
                return False
        return True
                
        
        