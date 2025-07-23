class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        points = 0
        a, b = 'a', 'b'
        
        if y > x:
            a, b = b, a
            x, y = y, x
        
        stack = []
        # First pass to remove 'ab' substrings
        for char in s:
            if char == b and stack and stack[-1] == a:
                stack.pop()
                points += x
            else:
                stack.append(char)
        
        # Second pass to remove 'ba' substrings from the remaining string
        remaining = []
        for char in stack:
            if char == a and remaining and remaining[-1] == b:
                remaining.pop()
                points += y
            else:
                remaining.append(char)
        
        return points