class OrderedStream:

    def __init__(self, n: int):
        self.map={i:"" for i in range(n)}
        self.ptr=0
    def insert(self, idKey: int, value: str) -> List[str]:
        res=[]
        self.map[idKey-1]=value
         
        
        while (self.ptr in self.map.keys()) and len(self.map[self.ptr])>0:
            res.append(self.map[self.ptr])
            self.ptr+=1
        return res

        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)