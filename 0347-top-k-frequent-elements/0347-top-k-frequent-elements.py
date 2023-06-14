class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for num in nums:
            if num not in hm:
                hm[num] = 1
            else:
                hm[num] += 1
        hmx = sorted(hm.items(), key=lambda kv: kv[1],reverse=True)
        print(hmx)
        res=[]
        for key,v in hmx:
            if k > 0:
                k-=1
                res.append(key)
        return res
        