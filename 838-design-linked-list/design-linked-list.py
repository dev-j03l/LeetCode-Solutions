class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        cur = self.head
        for _ in range(index):
            cur = cur.next

        return cur.val
        

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0 
        if index > self.size:
            return
        
        new_node = ListNode(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            if self.size == 0:
                self.tail = new_node
            self.size += 1
            return
        
        if index == self.size:
            if self.tail:
                self.tail.next = new_node
            else:
                self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        
        prev = self.head
        for _ in range(index - 1):
            prev = prev.next
        
        new_node.next = prev.next
        prev.next = new_node
        self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        if index == 0:
            removed = self.head
            self.head = self.head.next if self.head else None
            if self.head is None:
                self.tail = None
            self.size -= 1
            return
        
        prev = self.head
        for _ in range(index - 1):
            prev = prev.next
        removed = prev.next
        prev.next = removed.next
        if prev.next == None:
            self.tail = prev
        self.size -=1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)