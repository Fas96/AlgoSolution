class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        relSort=[]
        for el in arr2:
            while el in arr1:
                relSort.append(el)
                arr1.remove(el)
        return relSort+sorted(arr1)