from collections import Counter
class Solution(object):
    def lengthOfLongestSubstring(self, s): 
            if len(s) == 0:
                return 0
            Holds = {}
            maxLength = start = 0
            for i in range(len(s)):

                if s[i] in Holds and start <= Holds[s[i]]:
                    # print(Holds[s[i]],end= '   ')
                    start = Holds[s[i]] + 1
                    # print(start)
                else:
                    maxLength = max(maxLength, i - start + 1)
                Holds[s[i]] = i
            print(Holds)
            return maxLength