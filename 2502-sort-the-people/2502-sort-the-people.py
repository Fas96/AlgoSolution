class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        print(sorted(zip(names,heights),key=lambda x: x[1], reverse=True))
        return [a for a,b in sorted(zip(names,heights),key=lambda x: x[1], reverse=True)]
        