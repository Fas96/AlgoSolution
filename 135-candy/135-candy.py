class Solution:
    def candy(self, ratings: List[int]) -> int:
        # base condition
        n=len(ratings)
        if n<1:return 0
       
        dp=[1]*n
        
        for i in range(n-1):
            if ratings[i]<ratings[i+1]:
                dp[i+1]=max(dp[i]+1,dp[i+1])
        print(dp)
        for i in range(n-2,-1,-1):
            if ratings[i+1]<ratings[i]:
                dp[i]=max(dp[i+1]+1,dp[i])
                
        
        
        # L,R=0,1
#         while(R<n):
#             if ratings[L] < ratings[R]:
#                 dp[L+1]=max(dp[L]+1,dp[R])
#                 L+=1
#                 R+=1
#             elif ratings[L] > ratings[R]:
#                 dp[R]=max(dp[R]+1,dp[L])
#                 L+=1
#                 R+=1
#             else:
#                 L+=1
#                 R+=1
                
 
        return sum(dp)
    
     
            
            
        