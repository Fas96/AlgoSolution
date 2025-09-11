class Solution:
    def sortVowels(self, s: str) -> str:
        def isVowel(char):
            return char.lower() in 'aeiou'
        vow=[]
        for c in s:
            if  isVowel(c):
                vow.append(c)
        vow.sort()

        result = []
        vowel_index = 0
        
        for c in s:
            if isVowel(c):
                result.append(vow[vowel_index])
                vowel_index += 1
            else:
                result.append(c)
        return ''.join(result) 
        