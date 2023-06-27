class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        N1,N2,ans=len(nums1),len(nums2),[]
         
        mh=[(nums1[0]+nums2[0], 0, 0)]
        
        while mh and len(ans) < k:
            dump,idx,jdx=heapq.heappop(mh)
            ans.append((nums1[idx], nums2[jdx]))
            
            if jdx == 0 and idx+1 < len(nums1):
                heapq.heappush(mh, (nums1[idx+1]+nums2[jdx], idx+1, jdx))
            if jdx+1 < len(nums2):
                heapq.heappush(mh, (nums1[idx]+nums2[jdx+1], idx, jdx+1))
                
        return ans
        
        
        