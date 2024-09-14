class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        arr[:]=accumulate(arr, xor)
        ans=[0]*len(queries)
        for i, (q0, qN) in enumerate(queries):
            if q0==0:
                ans[i]=arr[qN]
            else:
                ans[i]=arr[qN]^arr[q0-1]
        return ans