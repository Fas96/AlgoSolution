class TwoSum:

    def __init__(self):
        self.arr=[]
        

    def add(self, number: int) -> None:
        self.arr.append(number)
        

    def find(self, value: int) -> bool:
        mp={}
        for i,x in enumerate(self.arr): 
            if x in mp:
                return True
            mp[value-x]=i 
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)