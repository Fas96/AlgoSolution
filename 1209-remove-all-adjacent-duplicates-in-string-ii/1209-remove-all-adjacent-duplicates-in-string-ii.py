class Solution(object):   
    def removeDuplicates(self, s, k):
        stack = [['_',0]]  # avoids empty stack check
        for c in s: 
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k: 
                    stack.pop()
            else: 
                stack.append([c, 1])
        return "".join(char*occurances for char,occurances in stack[1:])