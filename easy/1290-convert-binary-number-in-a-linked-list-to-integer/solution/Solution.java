/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
import java.util.*;
class Solution {
    public int getDecimalValue(ListNode head) {
        ArrayList<Integer> arr = new ArrayList<>();
        ListNode curr = head;
        while(curr!= null){
            arr.add(curr.val);
            curr = curr.next;
        }

        int res = 0;
        int j = 0;
        for(int i = arr.size()-1; i >= 0; i--){
            res += arr.get(i) * Math.pow(2, j);
            j++;
        }
        return (int) res;
    }
}