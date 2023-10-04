class MyHashMap:

    def __init__(self):
        self.map={}
        

    def put(self, key: int, value: int) -> None:
        self.map[key]=value
        return None
        

    def get(self, key: int) -> int:
        val=self.map.get(key) 
        return val if val is not None else -1

    def remove(self, key: int) -> None:
        if key in self.map:
            del self.map[key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)