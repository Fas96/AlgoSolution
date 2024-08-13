class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        ans=[]
        candidates.sort()
        def bt(idx,sm,ele):
            if sm==target:
                ans.append(ele[:])
                return
            if idx==n or sm>target:return
            ele.append(candidates[idx])
            bt(idx+1,sm+candidates[idx],ele)
            ele.pop()
            while idx+1<n and candidates[idx]==candidates[idx+1]:
                idx+=1
            bt(idx+1,sm,ele)
        bt(0,0,[])
        return ans