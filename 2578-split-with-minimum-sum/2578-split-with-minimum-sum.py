class Solution:
    def splitNum(self, num: int) -> int:
        keepVals =  [str(i) for i in str(num)]
        keepVals.sort()
        num1,num2="",""
        for i in range(len(keepVals)):
            if i%2==0:
                num1+=keepVals[i]
            else:
                num2+=keepVals[i]
        return int(num1)+int(num2)