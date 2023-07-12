class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome(left, right, changed):            
            while left < right:
                if s[left] != s[right]:
                    return isPalindrome(left + 1, right, True) or isPalindrome(left, right - 1, True) if not changed else False
                else:
                    left += 1
                    right -= 1
            return True

        return isPalindrome(0, len(s) - 1, False)
        