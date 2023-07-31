class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        mp=collections.defaultdict(int)
        m, n = len(s1), len(s2)
        for i in range(m):
            for j in range(n):
                if s1[i]==s2[j]:
                    mp[i,j]=mp[i-1,j-1]+ord(s1[i])
                else:
                    mp[i,j]=max(mp[i-1,j],mp[i,j-1])
        
        t_ascii=sum(map(ord,s1))+sum(map(ord,s2))
        return t_ascii-2*mp[m-1,n-1]