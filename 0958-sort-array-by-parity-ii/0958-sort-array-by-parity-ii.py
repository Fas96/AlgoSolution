class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        answer=[] 
        even = [n for n in nums if n%2 == 0]
        odd =  [n for n in nums if n%2 == 1]
 
        for a, b in zip(even, odd):
            answer.append(a)
            answer.append(b)
        
        return answer