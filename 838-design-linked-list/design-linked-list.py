class ListNode:
    def __init__(
        self,
        val: int = 0,
        prev: Optional[ListNode] = None,
        next: Optional[ListNode] = None
    ):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy = ListNode(0)
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.dummy.next
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        if index > self.size:
            return

        current = self.dummy.next
        for _ in range(index):
            current = current.next

        new_node = ListNode(val)
        prev_node = current.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = current
        current.prev = new_node
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        current = self.dummy.next
        for _ in range(index):
            current = current.next
        current.prev.next = current.next
        current.next.prev = current.prev
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)