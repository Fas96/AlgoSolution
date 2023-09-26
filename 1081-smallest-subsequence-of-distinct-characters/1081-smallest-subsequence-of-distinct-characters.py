class Solution:
    def smallestSubsequence(self, s: str) -> str:
        st=[]
        tk=set()
        mp = Counter(s)
        
        for i,c in enumerate(s): 
            if c not in tk:
                while st and st[-1]>c and mp[st[-1]]>0:
                    tk.remove(st.pop()) 
                st.append(c)
                tk.add(c)
            mp[c]-=1
        
        return ''.join(st)
        