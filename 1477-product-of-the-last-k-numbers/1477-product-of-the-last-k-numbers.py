from operator import mul

class ProductOfNumbers:
    def __init__(self):
        self.nms = [1]  

    def add(self, num: int) -> None:
        self.nms = [1] if num == 0 else self.nms + [self.nms[-1] * num]

    def getProduct(self, k: int) -> int:
        return 0 if k >= len(self.nms) else self.nms[-1] // self.nms[-(k+1)]
 