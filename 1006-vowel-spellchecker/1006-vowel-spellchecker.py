class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        exact=set(wordlist)
        case,vowel={},{}

        for i in wordlist:
            l=i.lower()
            if l not in case:
                case[l]=i 
            v="".join("*" if j in "aeiou" else j for j in l)
            if v not in vowel:
                vowel[v]=i

        r=[]
        for i in queries:
            if i in exact:
                r.append(i)
            else:
                l=i.lower()
                v="".join("*" if j in "aeiou" else j for j in l)
                if l in case:
                    r.append(case[l])
                elif v in vowel:
                    r.append(vowel[v])
                else:
                    r.append("")
        return r