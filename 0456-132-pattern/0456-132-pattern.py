class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        for num in nums:
            if not stack:
                stack.append((num, num))
                continue

            minimum = num
            while stack and stack[-1][1] < num:
                minimum = min(minimum, stack.pop()[0])

            if stack and stack[-1][0] < num < stack[-1][1]:
                return True

            stack.append((minimum, num))

        return False
        