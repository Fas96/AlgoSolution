class Solution:
    def nearestPalindromic(self, n: str) -> str:
        k = len(n)
        cands = {str(c:=pow(10,k)+1), str((c-1)//10-1)}         # The two edge-case candidates
                                                                # (e.g: "10001" and "999" 
                                                                #       for any 4-digit n)

        pref = (str(int(n[:(k + 1)//2])+i) for i in (-1,0,1))   # left sides of the remaining
                                                                # three candidates 
        for left in pref:
            rght = left[-2::-1] if k%2 else left[::-1]          # complete these three candidates 
            cands.add(left + rght)                              # with their right sides

        cands.discard(n)                                        # n is prohibited from candidacy

        return min(cands, key=lambda x:(abs(int(x) - int(n)), int(x)))