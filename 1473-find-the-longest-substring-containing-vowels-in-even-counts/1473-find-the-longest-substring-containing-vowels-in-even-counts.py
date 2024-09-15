class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
  
        mp={'a':0, 'e':1, 'i':2, 'o':3, 'u':4 }
        bmk_idx = {0: -1}  
        cur_bmk = 0
        ans = 0
        
        for i, char in enumerate(s):
            print(cur_bmk)
            if char in mp:
                cur_bmk ^= (1 << mp[char])  
            if cur_bmk in bmk_idx: 
                ans = max(ans, i - bmk_idx[cur_bmk])
            else:
                bmk_idx[cur_bmk] = i
        
        return ans
        