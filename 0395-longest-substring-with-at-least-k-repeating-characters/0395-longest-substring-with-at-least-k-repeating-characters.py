class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        count = Counter(s)
        max_len = 0 
        for char in count:
            if count[char] < k: 
                for part in s.split(char):
                    max_len = max(max_len, self.longestSubstring(part, k))
                return max_len 
        return len(s)