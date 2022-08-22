class Solution {
    public int secondsToRemoveOccurrences(String s) {
          int res=0;
   
    while (s.contains("01")){
     if(s.contains("01")){
      
       s=s.replaceAll("01","10");
       res++;
     }else{
       break;
     }
    }
    return res;
    }
}