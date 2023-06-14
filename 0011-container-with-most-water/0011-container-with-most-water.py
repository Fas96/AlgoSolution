class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R = 0, len(height)-1
        maxWater = 0

        while L < R:
            W = R - L
            H = min(height[L], height[R])
            areaOfWater = W * H
            maxWater = max(maxWater, areaOfWater)
            if height[L] > height[R]:
                R -= 1
            else:
                L += 1
        return maxWater