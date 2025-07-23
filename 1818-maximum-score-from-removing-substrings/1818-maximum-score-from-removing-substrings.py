class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        points = 0
        
        def remove_substrings(s, sub, point):
            nonlocal points
            stack = []
            for char in s:
                stack.append(char)
                if len(stack) >= 2 and stack[-2] + stack[-1] == sub:
                    stack.pop()
                    stack.pop()
                    points += point
            return ''.join(stack)
        
        if y > x:
            s = remove_substrings(s, 'ba', y)
            s = remove_substrings(s, 'ab', x)
        else:
            s = remove_substrings(s, 'ab', x)
            s = remove_substrings(s, 'ba', y)
        
        return points