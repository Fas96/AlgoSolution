class Solution {
    public int minimumSum(int num) {
            List<Integer> sb=new ArrayList<>();
        while (num>0){
            sb.add(num%10);
            num/=10;
        }

        sb.sort(Integer::compareTo);


       int n=sb.size();

        return Integer.parseInt(sb.get(0)+""+sb.get(n-1)) + Integer.parseInt(sb.get(1)+""+sb.get(n-2));

    }
}