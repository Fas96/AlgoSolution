class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp=defaultdict(int)
        mp[0]=-1
        ans=0
        curs=0
        for i,x in enumerate(nums):
            if x==1:
                curs+=1
            else:
                curs-=1
    
            if curs in mp:
                ans=max(ans,i-mp[curs])
            else:
                mp[curs]=i

        return ans
        