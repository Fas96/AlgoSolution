class Solution:
    @cache
    def parseBoolExpr(self, expression: str) -> bool:
        if expression[0] == '&':
            return all(map(self.parseBoolExpr, self.split(expression[2:-1])))
        if expression[0] == '|':
            return any(map(self.parseBoolExpr, self.split(expression[2:-1])))
        if expression[0] == '!':
            return not self.parseBoolExpr(expression[2:-1])
        if expression == 'f':
            return False
        if expression == 't':
            return True
    
    def split(self, expression: str) -> List[str]:
        opened = 0
        prev = 0
        res = []
        for i in range(len(expression)):
            if expression[i] == '(':
                opened += 1
            elif expression[i] == ')':
                opened -= 1
            
            if expression[i] == ',' and not opened:
                res.append(expression[prev:i])
                prev = i+1
        res.append(expression[prev:i+1])
        return res