class MapSum:

    def __init__(self):
        self.mp={}
        

    def insert(self, key: str, val: int) -> None:
        self.mp[key]=val
        

    def sum(self, prefix: str) -> int:
        sm=0
        for k,v in self.mp.items():
            if k.startswith(prefix):
                sm+=v
        return sm
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)