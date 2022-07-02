class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        def maxG(n,mx):
            mx=max(n[0],mx-n[-1])
            for i in range(1,len(n)):
                mx=max(mx,n[i]-n[i-1])
            return mx
        return maxG(sorted(horizontalCuts),h)*maxG(sorted(verticalCuts),w)%1000000007
 