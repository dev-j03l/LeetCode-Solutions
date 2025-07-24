import java.util.*;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> pairs = new HashMap<>();
        
        pairs.put('(', ')');
        pairs.put('[', ']');
        pairs.put('{', '}');

        for (int i = 0; i < s.length(); i++) {
            char current = s.charAt(i);

            if (pairs.containsKey(current)) {
                stack.push(current);
            } else {
                if (stack.isEmpty()) return false;
                char top = stack.pop();
                if (pairs.get(top) != current) return false;
            }
        }

        return stack.isEmpty();
    }
}
