import java.util.*;
class MyStack {
    ArrayDeque<Integer> q1;
    ArrayDeque<Integer> q2;

    public MyStack() {
        q1 = new ArrayDeque<Integer>();
        q2 = new ArrayDeque<Integer>();    
    }
    
    public void push(int x) {
        while(!q1.isEmpty()){
            q2.addLast(q1.pollFirst());
        }
        q1.addLast(x);
        while(!q2.isEmpty()){
            q1.addLast(q2.pollFirst());
        }
    }
    
    public int pop() {
        if(q1.isEmpty()) return -1;
        return q1.pollFirst();
    }
    
    public int top() {
        return q1.peekFirst();
    }
    
    public boolean empty() {
        return q1.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */