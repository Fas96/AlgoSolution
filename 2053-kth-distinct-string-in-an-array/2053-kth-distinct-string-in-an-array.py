class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        darr = Counter(arr)
        res = []
        for a, v in darr.items():
            if v == 1:
                res.append(a)
        output=res[k - 1] if len(res) >= k else ""

        return output