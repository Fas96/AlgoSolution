class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        sm=sum(apple)
        ac=sorted(capacity,reverse=True)
        rs=list(accumulate(ac))
        for i,v in enumerate(rs):
            if v>=sm:
                return i+1

        return -1
        