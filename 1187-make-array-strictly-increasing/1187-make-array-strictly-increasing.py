import bisect
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int: 
        arr2 = sorted(set(arr2))
        n1, n2 = len(arr1), len(arr2)

        d = {0: arr1[0]}  # swap time: value of last
        if arr2[0] < arr1[0]:
            d[1] = arr2[0]
        
        for i in range(1, n1):
            new_d = {}
            x = arr1[i]
            for time, value in d.items():
                if value < x:
                    new_d[time] = x
            for time, value in d.items():
                index = bisect.bisect_right(arr2, value)  
                if index < n2:
                    if time + 1 in new_d:
                        new_d[time + 1] = min(new_d[time + 1], arr2[index])
                    else:
                        new_d[time + 1] = arr2[index]
            
            d = new_d
        return min(d.keys()) if d else -1 
        