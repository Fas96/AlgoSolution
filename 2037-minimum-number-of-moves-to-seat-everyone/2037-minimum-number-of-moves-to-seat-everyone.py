class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        ans=0
        seats.sort()
        students.sort()
        for i in range(len(seats)):
            ans+=abs(students[i]-seats[i])
        return ans