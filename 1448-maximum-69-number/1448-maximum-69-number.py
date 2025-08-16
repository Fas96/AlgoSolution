class Solution:
    def maximum69Number (self, num: int) -> int:
        ans=num
        df=defaultdict(list) 
        for i,v in enumerate(str(num)): 
            df[v].append(i)
        ll=list(str(num))
        if df['6']:
            for i in df.get('6'):
                ll[i]='9'
                ans=max(ans,int("".join(ll)))
                ll[i]='6'
        return ans
        