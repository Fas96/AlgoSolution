class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        mp="abcdefghijklmnopqrstuvwxyz"
        while len(word)<k:
            for c in word:
                word+=mp[(mp.index(c)+1)%26] 
        return word[k-1]