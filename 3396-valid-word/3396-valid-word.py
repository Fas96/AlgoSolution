class Solution:
    def isValid(self, word: str) -> bool:
        vowelCount,consonantCount=0,0
        vowels="aeiou"
        conso="bcdfghjklmnpqrstvwxyz"
        for c in word:
            if   c.isalnum():
                if c.lower() in vowels:
                    vowelCount+=1
                elif  c.lower() in conso:
                    consonantCount+=1
            else:
                return False 
        if vowelCount<1: return False
        if consonantCount<1: return False

        if len(word)<3: return False
        
        return True

        