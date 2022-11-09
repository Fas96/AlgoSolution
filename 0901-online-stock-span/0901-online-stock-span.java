class StockSpanner {

   Stack<int[]> stocks;

    public StockSpanner() {
        stocks = new Stack<>();
        
    }
    public int next(int price) {
        int res = 1;
        while (!stocks.isEmpty() && stocks.peek()[0] <= price) {
            res += stocks.pop()[1];
        }
        stocks.push(new int[]{price, res});
        return res;
    }
}

/**
TLE
--------
List<Integer> stocks;

    public StockSpanner() {
        stocks= new LinkedList<>();
    }

    public int next(int price) {
        this.stocks.add(price); 
        int count=0;
        for(int i=stocks.size()-1;i>=0;i--){
            if(stocks.get(i)<=price){
                count++;
            }else{
                break;
            }
        }
        return count;
    }
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.next(price);
 */