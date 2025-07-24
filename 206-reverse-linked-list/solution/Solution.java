
class Solution {
    public ListNode reverseList(ListNode head) {   
        ListNode current = head;
        ListNode follower = null;
        while(current != null){
            ListNode next = current.next;
            current.next = follower;
            follower = current; 
            current = next;
        }
        return follower;
    }
}
