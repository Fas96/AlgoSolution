class Solution:
    def maxDistance(self, pos: List[int], m: int) -> int:
        pos.sort()
        n=len(pos)
        low=1
        high=pos[-1]-pos[0]
        while low<=high:
            mid,balls_loc,prev_pos=(low+high)//2,1,pos[0] 
            for i in range(1,n):
                if pos[i]-prev_pos>=mid:
                    balls_loc+=1
                    prev_pos=pos[i]
            if balls_loc>=m:
                low=mid+1
                maxForce=mid
            else:
                high=mid-1
        return maxForce