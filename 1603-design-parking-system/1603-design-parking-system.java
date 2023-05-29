class ParkingSystem {

   Map<Integer,Integer> parkingMap;

        public ParkingSystem(int big, int medium, int small) {
            parkingMap = new  HashMap<>();
            
            parkingMap.put(1,big);
            parkingMap.put(2,medium);
            parkingMap.put(3,small);
        }

        public boolean addCar(int carType) {
            if(parkingMap.get(carType) > 0){
                parkingMap.put(carType,parkingMap.get(carType) - 1);
                return true;
            }
            return false;
        }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * boolean param_1 = obj.addCar(carType);
 */