class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        cn=defaultdict(int)
        for x in emails:
            ff=x.split("@")
            mail=ff[0]
            f=mail.replace(".","").split("+")[0]+"@"+ff[1]
            if f in cn:
                cn[f]+=1
            else:
                cn[f]=1
        return len(cn)
        