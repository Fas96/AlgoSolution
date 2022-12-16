class MyQueue {

    Stack<Integer> back= null; 
    Stack<Integer> front=null;
 

    public MyQueue() {
        back=new Stack<>();
        front= new Stack<>();
    }

    public void push(int x) {
        front.push(x);
    }

    public int pop() {
       if (back.size()==0){
           while (front.size()>0) back.add(front.pop());
       }
        return back.pop();
    }

    public int peek() {
        if (back.size()==0){
            while (front.size()>0) back.add(front.pop());
        }
        return  back.peek();
    }

    public boolean empty() {
        return back.size()+front.size()==0;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */