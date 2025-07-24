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

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // Lets do a check to see if list1 or list2 are empty
        if(list1 == null){
            return list2;
        }
        if(list2 == null){
            return list1;
        }
        
        ListNode head;
        if(list1.val < list2.val){
            head = list1;
            list1 = list1.next;
        } else {
            head = list2;
            list2 = list2.next;
        }
        ListNode iterator = head;
        while(list1 != null && list2 != null){
            if(list1.val <= list2.val){
                iterator.next = list1;
                list1 = list1.next;
            } else{
                iterator.next = list2;
                list2 = list2.next;
            }
            iterator = iterator.next;
        }

        iterator.next = (list1 != null) ? list1 : list2;
        return head;

    }
}