class BrowserHistory {
     Deque<String> forwardStack;
    Deque<String> backStack;
    String currentUrl;

    public BrowserHistory(String homepage) {
        forwardStack = new ArrayDeque<>();
        backStack = new ArrayDeque<>();
        currentUrl = homepage;
    }
 
    
   
    public void visit(String url) {
        backStack.push(currentUrl);
        currentUrl = url;
        forwardStack.clear();
    }
    
    public String back(int steps) {
        while (steps > 0 && !backStack.isEmpty()) {
            forwardStack.push(currentUrl);
            currentUrl = backStack.pop();
            steps--;
        }
        return currentUrl;
    }
    
    public String forward(int steps) {
        while (steps > 0 && !forwardStack.isEmpty()) {
            backStack.push(currentUrl);
            currentUrl = forwardStack.pop();
            steps--;
        }
        return currentUrl;
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = new BrowserHistory(homepage);
 * obj.visit(url);
 * String param_2 = obj.back(steps);
 * String param_3 = obj.forward(steps);
 */