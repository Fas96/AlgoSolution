class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums[0])
        s="0"*n
        nums=set(nums)
        q=deque([s])
        lookup=set()
        while q:
            curr=q.popleft()
            if curr not in nums:
                return curr
            lookup.add(curr)
            for i in range(n):
                if s[i]=="0":
                    if  s[:i]+"1"+s[i+1:] not in lookup:
                        q.append(s[:i]+"1"+s[i+1:])
        