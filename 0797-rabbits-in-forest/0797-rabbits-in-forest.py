class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        return sum((f+x)//(x+1)*(x+1) for x, f in Counter(answers).items())