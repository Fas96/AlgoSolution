class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res=float("-inf")
        for i in range(len(number)):
            if number[i]==digit:
                remove=number[:i]+number[i+1:]
                res=max(res,int(remove))
        return str(res)
        