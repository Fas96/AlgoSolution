class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [Counter()]
        i = 0
        n = len(formula)
        
        while i < n:
            if formula[i] == '(': 
                stack.append(Counter())
                i += 1
            elif formula[i] == ')': 
                i += 1 
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[start:i] or 1) 
                top = stack.pop()
                for elem, count in top.items():
                    stack[-1][elem] += count * multiplier
            else: 
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                elem = formula[start:i] 
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[start:i] or 1) 
                stack[-1][elem] += count
         
        result = stack.pop() 
        sorted_elements = sorted(result.items()) 
        output = []
        for elem, count in sorted_elements:
            output.append(elem)
            if count > 1:
                output.append(str(count))
        
        return ''.join(output)