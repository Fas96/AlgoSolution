class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.v = [big,medium,small] 
    def addCar(self, carType): 
        if carType==1 and self.v[0]>0:
            self.v[0]-=1
            return True
        elif carType==2 and self.v[1]>0:
            self.v[1]-=1
            return True
        elif carType==3 and self.v[2]>0:
            self.v[2]-=1
            return True
        return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)