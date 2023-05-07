class Solution {
    public boolean backspaceCompare(String s, String t) {
      int idx1=s.length()-1,idx2=t.length()-1;
        while (idx1>=0||idx2>=0){
            int i1=getNextValidCharIdx(s,idx1);
            int i2=getNextValidCharIdx(t,idx2);
            if(i1<0&&i2<0){
                return true;
            }
            if(i1<0||i2<0){
                return false;
            }
            if(s.charAt(i1)!=t.charAt(i2)){
                return false;
            }
            idx1=i1-1;
            idx2=i2-1;
        }
        return true;

    }

    private int getNextValidCharIdx(String str, int index) {
        int backspaceCount=0;
        while (index>=0){
            if(str.charAt(index)=='#'){
                backspaceCount++;
            }else if(backspaceCount>0){
                backspaceCount--;
            }else{
                break;
            }
            index--;
        }
        return index;
    }
}