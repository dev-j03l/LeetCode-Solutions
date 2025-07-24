import java.util.*;
class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        Stack<Integer> stack = new Stack<Integer>();
        ArrayDeque<Integer> line = new ArrayDeque<Integer>();

        for(int i = sandwiches.length-1; i >= 0; i--){
            stack.push(sandwiches[i]);
        }

        for(int student: students){
            line.addLast(student);
        }

        int studentsRotated = 0;
        while(studentsRotated < line.size() && !line.isEmpty()){
            if(line.peekFirst() == stack.peek()){
                stack.pop();
                line.pollFirst();
                studentsRotated = 0;
            } else{
                line.addLast(line.pollFirst());
                studentsRotated += 1; 
            }
        }

        return line.size();
    }
}