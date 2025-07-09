class ListNode{
    public ListNode next;
    public ListNode prev;
    public int val;

    ListNode(int val){
        this(null, null, val);
    }

    ListNode(ListNode next, ListNode prev, int val){
        this.next = next; this.prev = prev;
        this.val = val;
    }
}

class MyLinkedList {
    ListNode head;
    ListNode tail;
    int size;

    public MyLinkedList() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }
    
    public int get(int index) {
        if(index < 0 || index >= size) return -1; // invalid index
        ListNode current = head;
        for(int i = 0; i < index; i++){
            current = current.next;
        }
        return current.val;
    }
    
    public void addAtHead(int val) {
        ListNode newNode = new ListNode(val); // create a newNode
        if(head == null){
            head = newNode;
            tail = newNode;
        } else {
            newNode.next = head;
            head.prev = newNode;
            head = newNode;
        }
        size++;
    }
    
    public void addAtTail(int val) {
        if(head == null) addAtHead(val);
        else{
            ListNode newNode = new ListNode(val);
            newNode.prev = tail;
            tail.next = newNode;
            tail = newNode;
            size++; 
        }
    }
    
    public void addAtIndex(int index, int val) {
        if(index < 0 || index > size) return;

        if(index == 0) {
            addAtHead(val);
            return;
        }

        if(index == size) {
            addAtTail(val);
            return;
        }

        ListNode current = head;
        for(int i = 0; i < index; i++) {
            current = current.next;
        }

        ListNode newNode = new ListNode(val);
        newNode.prev = current.prev;
        newNode.next = current;
        current.prev.next = newNode;
        current.prev = newNode;

        size++;
    }

    public void deleteAtIndex(int index) {
        if (index < 0 || index >= size) return;

        ListNode current = head;
        if(current == null) return;
        for (int i = 0; i < index; i++) {
            current = current.next;
        }

        // Unlink current from list
        if (current.prev != null) {
            current.prev.next = current.next;
        } else {
            head = current.next; // deleting head
        }

        if (current.next != null) {
            current.next.prev = current.prev;
        } else {
            tail = current.prev; // deleting tail
        }

        size--;
    }

}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */