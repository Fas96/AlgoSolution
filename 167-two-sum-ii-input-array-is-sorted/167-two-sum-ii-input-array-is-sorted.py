class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        i=0
        j=len(numbers)-1
        
        while i<j:
            su=numbers[i]+numbers[j]
            
            if su==target:
                return [i+1,j+1]
            if su>target:
                j-=1
            else:
                i+=1
        return []
        