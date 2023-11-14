class Solution(object):
    def countPalindromicSubsequence(self, s):
        char_indices = {}
        for i, char in enumerate(s):
            if char not in char_indices:
                char_indices[char] = []
            char_indices[char].append(i)

        count = 0
        for indices in char_indices.values():
            if len(indices) > 1:
                unique_chars = set(s[min(indices)+1:max(indices)])
                count += len(unique_chars)
        return count