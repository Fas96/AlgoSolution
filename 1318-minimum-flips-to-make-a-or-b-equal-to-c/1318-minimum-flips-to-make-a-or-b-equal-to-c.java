class Solution {
    public int minFlips(int a, int b, int c) {
         int totalFlips=0;

        while (a>0 || b>0 || c>0){
            int Abit=1&a;
            int Bbit=1&b;
            int Cbit=1&c;

            if((Abit | Bbit) !=Cbit){ 
                if(Cbit==1){
                    totalFlips++;
                }else{
                    if(Abit==1 && Bbit==1)totalFlips+=2;
                    else if (Abit==1 || Bbit==1) totalFlips++;
                }
            }
            a>>=1;
            b>>=1;
            c>>=1;
        }
        return totalFlips;
    }
}