import java.util.*;
class MinStack {
    Stack<Integer> stack = new Stack<Integer>();
    Stack<Integer> minStack = new Stack<Integer>();

    public MinStack() {
    }
    
    public void push(int val) {
        stack.push(val);
        if(minStack.isEmpty() || val < minStack.peek()){
            minStack.push(val);
        }else{
            minStack.push(minStack.peek());
        }
    }
    
    public void pop() {
        stack.pop();
        minStack.pop();  
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
