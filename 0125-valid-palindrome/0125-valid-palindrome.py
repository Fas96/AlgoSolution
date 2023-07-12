class Solution:
    def isPalindrome(self, s: str) -> bool:
        conv= re.sub('[^0-9a-zA-Z]', '', s).lower()   
        return conv.find(conv[::-1])==0 