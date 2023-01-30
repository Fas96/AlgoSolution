class Solution {
    public int minFlipsMonoIncr(String s) {
        int n = s.length();
       int flip0 = 0;
       int flip1 = 0;
        
       for(int i=0;i<n;i++){
           if(s.charAt(i) == '0'){
               flip1 = Math.min(flip0, flip1)+1;
           } else {
               flip1 = Math.min(flip0, flip1);
               flip0++;
           }
       }
       return Math.min(flip0, flip1);
        // int indexFirst1 = s.indexOf('1');
        // if(indexFirst1 == -1) return 0;
        // String s1 = s.substring(indexFirst1);
        // //00011000
        // int count0 = 0;
        // for(int i=0;i<s1.length();i++){
        //     if(s1.charAt(i) == '0') count0++;
        // }
        // int count1 = 0;
        // for(int i=0;i<s1.length();i++){
        //     if(s1.charAt(i) == '1') count1++;
        // }
        // return Math.min(count0, count1);
    }
    // @Test
    // public void test() {
    //     int res = minFlipsMonoIncr("010110");
    //     // f1=1, f0=0
    //     // f1=0, f0=1
    //     // f1=1, f0=1
    //     // f1=2, f0=1
    //     // f1=1, f0=2
    //     // f1=2, f0=2
    //     Assert.assertEquals(2, res);
    //     res = minFlipsMonoIncr("00011000");
    //     Assert.assertEquals(2, res);
    //     //00110
    //     res = minFlipsMonoIncr("00110");
    //     //f1=1, f0=0
    //     //f1=1, f0=0
    //     //f1=0, f0=1
    //     //f1=0, f0=2
    //     //f1=1, f0=2
    //     Assert.assertEquals(1, res);
    // // }
}