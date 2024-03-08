class MyHashSet:

    def __init__(self):
        self.mp={}
        

    def add(self, key: int) -> None:
        self.mp[key]=[]
        

    def remove(self, key: int) -> None:
        if key in self.mp:
            del self.mp[key]
        

    def contains(self, key: int) -> bool:
        return key in self.mp
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)