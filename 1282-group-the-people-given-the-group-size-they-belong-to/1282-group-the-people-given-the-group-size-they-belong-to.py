class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]: 
        mp=defaultdict(list)
        ans=[]
        for i, size in enumerate(groupSizes):
            if size not in mp:
                mp[size]=[]
            mp[size].append(i)
            if len(mp[size]) == size:
                ans.append(mp[size])
                mp[size] = []
      
        return ans
        