class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        df={}
        st=[]
        for p in paths:
            if p[0] not in st:
                st.append(p[0])
            if p[1] not in st:
                st.append(p[1])
            if p[0] not in df:
                df[p[0]]=[p[1]]
            else:
                df[p[0]].append(p[1])
      
        dfl=[k for k,v in df.items()] 
     
        for val in st:
            if val not in dfl:
                return val
        return ''
                
                
        