class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        start=1
        ans=[]
        
        for val in target:
            if val==start:
                ans.append("Push")
                start+=1
            else:
                while start!=val:
                    ans.append("Push")
                    ans.append("Pop")
                    start+=1
                ans.append("Push")
                start+=1
                
        return ans