class Solution:
    def compareVersion(self, V1: str, V2: str) -> int:
        v1=[int(k) for k in V1.split('.')]
        v2=[int(k) for k in V2.split('.')]
        ml,mx=min(len(v1),len(v2)),max(len(v1),len(v2))
        if len(v1)!=mx:
            v1=v1+[0]*(mx-ml)
        if len(v2)!=mx:
            v2=v2+[0]*(mx-ml)
         
        for i in range(len(v1)):
            if v1[i]<v2[i]:return -1
            elif v1[i]>v2[i]:return 1
        return 0