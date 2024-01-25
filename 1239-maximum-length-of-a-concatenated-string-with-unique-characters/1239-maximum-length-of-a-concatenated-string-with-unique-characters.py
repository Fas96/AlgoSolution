class Solution:
    def maxLength(self, a: List[str]) -> int:
        return (f:=lambda i,s:max(f(i+1,s),len(g:=s|{*a[i]})==len(s)+len(a[i]) and f(i+1,g)) if i<len(a) else len(s))(0,set())