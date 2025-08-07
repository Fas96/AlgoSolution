class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n=len(fruits)
        #IMP***The children will make exactly n - 1 moves***
        #child 1 has only 1 path i.e. diagonally
        child1_fruits = sum(fruits[i][i] for i in range(n))

        #child 2
        for i in range(n):
            for j in range(i + 1, n - (i + 1)):
                fruits[i][j] = 0
        
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                fruits[i][j] += max(
                    fruits[i - 1][j - 1], 
                    fruits[i - 1][j], 
                    fruits[i - 1][j + 1] if j + 1 < n else 0 )

        #child 3
        for j in range(n):
            for i in range(j + 1, n - (j + 1)):
                fruits[i][j] = 0

        for j in range(1, n - 1):
            for i in range(j + 1, n):
                fruits[i][j] += max(
                    fruits[i - 1][j - 1], 
                    fruits[i][j - 1], 
                    fruits[i + 1][j - 1] if i + 1 < n else 0 )
        
        return child1_fruits+fruits[-2][-1]+fruits[-1][-2]
        