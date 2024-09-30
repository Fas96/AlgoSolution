class CustomStack:

    def __init__(self, maxSize: int):
        self.stk=[]
        self.sz=maxSize
    def push(self, x: int) -> None:
        if len(self.stk)<self.sz:
            self.stk.append(x) 
    def pop(self) -> int:
        if len(self.stk)>0: 
            return self.stk.pop()

        return -1

    def increment(self, k: int, val: int) -> None:
        n = min(k,len(self.stk))
        for i in range(n):
            self.stk[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)