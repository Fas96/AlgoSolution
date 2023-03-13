class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int finalAnsAfterOpe=0;
        for (String operation : operations) {
            if (operation.contains("+"))finalAnsAfterOpe++;
            else finalAnsAfterOpe--;
            
        }
        return finalAnsAfterOpe;
    }
}