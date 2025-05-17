def hamming_distance(str1, str2):
        dist = 0
        if len(str1)!=len(str2):
            return False
            
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                dist += 1
        return dist

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        dp = [1]*len(words)
        prev = [-1]*len(words)

        for i in range(len(words)):
            for j in range(i):
                if groups[i] != groups[j] and hamming_distance(words[i], words[j]) == 1 and len(words[i]) == len(words[j]):
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j

        
        curr = dp.index(max(dp))

        res = []

        while curr != -1:
            res.append(words[curr])
            curr = prev[curr]
        return res[::-1]


        