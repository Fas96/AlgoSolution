class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(arr):
            if len(arr)>1:
                mid=len(arr)//2
                L,R=arr[:mid],arr[mid:]
                mergesort(L)
                mergesort(R)
                i=j=k=0
                while i<len(L) and j<len(R):
                    if L[i]<=R[j]:
                        arr[k]=L[i]
                        i+=1
                    else:
                        arr[k]=R[j]
                        j+=1
                    k+=1
                while i<len(L):
                    arr[k]=L[i]
                    i+=1
                    k+=1
                while j<len(R):
                    arr[k]=R[j]
                    j+=1
                    k+=1
        mergesort(nums)
        return nums
                
            