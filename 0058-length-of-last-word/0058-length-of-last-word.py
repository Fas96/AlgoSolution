class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wds=s.strip()
        print(wds)
        return len(s.strip().split(" ")[-1])
        