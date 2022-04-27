class Solution {
    public int convertTime(String current, String correct) {
        
        int r=0;
       int[] op=new int[] {  1, 5, 15,  60};
        String[] currentTime = current.split(":");
        String[] correctTime = correct.split(":");

        int hourdiff=Integer.parseInt(correctTime[0])-Integer.parseInt(currentTime[0]);
        int minDiff=Integer.parseInt(correctTime[1])-Integer.parseInt(currentTime[1]);
        int TotalTimeneeded= (hourdiff *60)+minDiff;
 
        int minSum=Integer.MAX_VALUE;

         while(TotalTimeneeded!=0){
            if(TotalTimeneeded>=op[3]){
                TotalTimeneeded-=op[3];
                r++;
            }
            else if(TotalTimeneeded>=op[2]){
                TotalTimeneeded-=op[2];
                r++;
            }
            else if(TotalTimeneeded>=op[1]){
                TotalTimeneeded-=op[1];
                r++;
            }
            else if(TotalTimeneeded>=op[0]){
                TotalTimeneeded-=op[0];
                r++;
            }
        }




        return r;
    }
}