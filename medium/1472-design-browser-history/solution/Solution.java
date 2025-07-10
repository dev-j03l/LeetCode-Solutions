class Page{
    String url;
    Page next;
    Page prev;

    Page(String url){
        this(url, null, null);
    }

    Page(String url, Page next, Page prev){
        this.url = url;
        this.next = next;
        this.prev = prev;
    }
}

class BrowserHistory {
    private Page head;
    private Page tail;
    private Page current;

    public BrowserHistory(String homepage) {
        head = new Page(homepage);
        tail = head;
        current = head;
    }
    
    public void visit(String url) {
        // 1st cut off forward history
        current.next = null;
        
        // Create a newpage
        Page newPage = new Page(url);
        newPage.prev = current;
        current.next = newPage;
        tail = newPage;
        current = tail; //Move to newPage
    }
    
    public String back(int steps) {
        for(int i = 0; i < steps; i++){
            if(current.prev == null) break;
            current = current.prev;
        }
        return current.url;
    }
    
    public String forward(int steps) {
        for(int i = 0; i < steps; i++){
            if(current.next == null) break;
            current = current.next;
        }
        return current.url;
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = new BrowserHistory(homepage);
 * obj.visit(url);
 * String param_2 = obj.back(steps);
 * String param_3 = obj.forward(steps);
 */