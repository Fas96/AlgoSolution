class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        an=[]
        for x in arr:
            if arr.count(x)==1:
                an.append(x)
       
        return an[k-1] if k<=len(an) else ""