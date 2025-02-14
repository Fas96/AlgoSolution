from itertools import accumulate
from operator import mul

class ProductOfNumbers:
    def __init__(self):
        self.nms = [1]  
    def add(self, num: int) -> None:
        if num == 0:
            self.nms = [1]   
        else:
            self.nms.append(self.nms[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.nms):  
            return 0
        return self.nms[-1] // self.nms[-(k+1)]
 