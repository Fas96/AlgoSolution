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


        //while loop untill the diffrence will be 0
        while(TotalTimeneeded!=0){
            if(TotalTimeneeded>=60){
                TotalTimeneeded-=60;
                r++;
            }
            else if(TotalTimeneeded>=15){
                TotalTimeneeded-=15;
                r++;
            }
            else if(TotalTimeneeded>=5){
                TotalTimeneeded-=5;
                r++;
            }
            else if(TotalTimeneeded>=1){
                TotalTimeneeded-=1;
                r++;
            }
        } 




        return r;
    }
}