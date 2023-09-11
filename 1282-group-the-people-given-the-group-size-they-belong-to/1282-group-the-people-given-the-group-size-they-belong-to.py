class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        def chunks(xs, n):
            n = max(1, n)
            return (xs[i:i+n] for i in range(0, len(xs), n))
        
        mp=defaultdict(list)
        for i in range(len(groupSizes)):
            if groupSizes[i] in mp:
                mp[groupSizes[i]].append(i)
            else:
                mp[groupSizes[i]]=[i]
        ans=[]
        for key,val in mp.items():
            if len(val)>key:
                for x in chunks(val,key): 
                    ans.append(x)
            else:
                ans.append(val)
        return ans
        