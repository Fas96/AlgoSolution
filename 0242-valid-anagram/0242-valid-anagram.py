class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        shm=Counter(s)
        thm=Counter(t)
        return shm==thm
        