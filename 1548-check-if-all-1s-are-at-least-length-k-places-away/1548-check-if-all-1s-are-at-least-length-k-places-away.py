class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        zlen=0
        arr=[]
        for i in nums:
            if i==0:
                zlen+=1
            else:
                arr.append(zlen)
                zlen=0
        arr.append(zlen)
         
        print(arr[1:len(arr)-1])
        return all(x>=k for x in arr[1:len(arr)-1])
            
            
        