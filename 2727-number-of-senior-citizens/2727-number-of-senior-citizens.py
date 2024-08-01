class Solution:
    def countSeniors(self, details: List[str]) -> int: 
        return sum([1 for x in details if int(x[11:13])>60  ])
        