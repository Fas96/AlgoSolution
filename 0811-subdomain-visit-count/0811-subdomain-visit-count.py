class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans=[]
        hs=defaultdict(int)
        for url in cpdomains:
            cnt,dom=url.split(" ") 
            abc=dom.split(".")
            for x in range(len(abc)):
                key=".".join(abc[x:])
                if key not in hs:
                    hs[key]=int(cnt)
                    ans.append(str(hs[key])+" "+key)
                else:
                    ans.remove(str(hs[key])+" "+key)
                    hs[key]+=int(cnt)
                    ans.append(str(hs[key])+" "+key)

        return ans
        