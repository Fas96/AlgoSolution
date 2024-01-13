class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ans = 0
        hashh = [0] * 26

        # Count occurrences of each character in string s
        for ch in s:
            hashh[ord(ch) - ord('a')] += 1

        # Update occurrences based on string t and calculate steps
        for ch in t:
            hashh[ord(ch) - ord('a')] -= 1
            if hashh[ord(ch) - ord('a')] < 0:
                ans += 1

        return ans
        
        
        