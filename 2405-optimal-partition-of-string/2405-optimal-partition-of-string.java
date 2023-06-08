class Solution {
    public int partitionString(String s) {
         int idx=0;
        int countPartition=1;
        Set<Character> chrHolders=new HashSet<>();
        while (idx<s.length()){
            if(!chrHolders.contains(s.charAt(idx))){
                chrHolders.add(s.charAt(idx));
            }else {
                countPartition++;
                chrHolders=new HashSet<>();
                chrHolders.add(s.charAt(idx));
            }
            idx++;
        }
        return countPartition;
    }
}