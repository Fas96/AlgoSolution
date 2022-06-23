class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        priorityQueues = []
        sumIndexZeros = 0
        sortBylastDayi=sorted(courses, key=lambda course: course[1])
        for durationi, lastDayi in sortBylastDayi:
            sumIndexZeros += durationi
            heapq.heappush(priorityQueues, -durationi)
            while sumIndexZeros > lastDayi:
                sumIndexZeros += heapq.heappop(priorityQueues)
        return len(priorityQueues)