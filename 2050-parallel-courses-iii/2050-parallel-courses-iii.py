class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        in_degree = [0] * n

        for relation in relations:
            prev_course, next_course = relation
            graph[prev_course - 1].append(next_course - 1)
            in_degree[next_course - 1] += 1

        min_heap = []
        for i in range(n):
            if in_degree[i] == 0:
                heapq.heappush(min_heap, (time[i], i))

        while min_heap:
            course_time, current_course = heapq.heappop(min_heap)

            for next_course in graph[current_course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    heapq.heappush(min_heap, (course_time + time[next_course], next_course))

        return course_time
        