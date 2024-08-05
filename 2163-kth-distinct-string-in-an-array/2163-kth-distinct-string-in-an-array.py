class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        for w, f in Counter(arr).items():
            if f == 1:
                k -= 1
                if not k:
                    return w
        return ""