import java.util.*;
class Node{
    int key;
    int val;
    Node next;
    Node prev;

    Node(int key, int val){
        this(key, val, null, null);
    }

    Node(int key, int val, Node prev, Node next){
        this.key = key;
        this.val = val;
        this.prev = prev;
        this.next = next;
    }
}

class LRUCache {
    Node head;
    Node tail;
    HashMap<Integer, Node> nodeMap;
    int cap;

    public LRUCache(int capacity) {
        this.cap = capacity;
        this.head = null;
        this.tail = null;
        this.nodeMap = new HashMap<>();
    }

    private void remove(Node node){
        // Remove should just delete the node from existence in our DLL
        if(node == null || head == null) return;

        if(head == tail && node == head) {
            head = tail = null;
            return;
        }

        if(node == head){
            head = head.next;
            if(head != null) head.prev = null;
        } else if (node == tail){
            tail = tail.prev;
            if(tail != null) tail.next = null;
        } else{
            node.prev.next = node.next;
            node.next.prev = node.prev;
        }

        node.next = null;
        node.prev = null;
    }

    private void insertTail(Node node){
        if(node == null) return;
        if(head == null){
            head = tail = node;
        } else{
            tail.next = node;
            node.prev = tail;
            tail = node;
        }
        node.next = null;
    }
    
    public int get(int key) {
        // Our get and put methods will need to modify our DLL
        // If we get or put it should move the accessed node to
        // the tail. We need a remove and insert method
        if(nodeMap.containsKey(key)){
            Node curr = nodeMap.get(key); // this should return the node
            remove(curr);
            insertTail(curr);
            return curr.val;
        } else{
            return -1;
        }
    }
    
    public void put(int key, int value) {
        if(nodeMap.containsKey(key)){
            Node curr = nodeMap.get(key);
            remove(curr);
            insertTail(curr);
            curr.val = value;
        } else {
            if(nodeMap.size() >= cap){
                if(head != null){
                    nodeMap.remove(head.key);
                    remove(head);
                }
            } 
            Node curr = new Node(key, value);
            nodeMap.put(key, curr);
            insertTail(curr);
        }
    }
}
