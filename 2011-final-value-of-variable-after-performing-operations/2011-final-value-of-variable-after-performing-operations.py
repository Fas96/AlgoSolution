class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        i = 0
        cnt=0
        while i< len(operations):
            if operations[i][0]=="+" or operations[i][2]=="+":
                cnt+=1
            else:
                cnt-=1
            i+=1
        return cnt
                