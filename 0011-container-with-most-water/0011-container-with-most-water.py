class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R = 0, len(height)-1
        maxWater = 0

        while L < R: 
            areaOfWater = (R - L) *min(height[L], height[R])
            maxWater = max(maxWater, areaOfWater)
            if height[L] > height[R]:
                R -= 1
            else:
                L += 1
        return maxWater