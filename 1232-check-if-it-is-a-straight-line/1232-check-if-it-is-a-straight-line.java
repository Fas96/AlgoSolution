class Solution {
    public boolean checkStraightLine(int[][] coordinates) {
            
        int iniXCod = coordinates[1][0] - coordinates[0][0];
        int iniYCode = coordinates[1][1] - coordinates[0][1];
        for (int i = 1; i < coordinates.length; i++) {
            double ydif=coordinates[i][1]-coordinates[i-1][1];
            double xdif=coordinates[i][0]-coordinates[i-1][0];
            if(ydif * iniXCod != xdif * iniYCode) return false;
        }

        return true;
    }
}