class ListNode:
    def __init__(
        self,
        val : int = 0,
        prev : Optional["ListNode"] = None,
        next : Optional["ListNode"] = None
        ):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:
    def __init__(self):
        self.dummy = ListNode()
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size: return -1
        return self._node_before(index).next.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size: return
        prev_node = self._node_before(index)
        next_node = prev_node.next
        new_node = ListNode(val,prev_node,next_node)
        prev_node.next = new_node
        next_node.prev = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size: return
        prev_node = self._node_before(index)
        to_delete = prev_node.next
        next_node = to_delete.next
        prev_node.next = to_delete.next
        next_node.prev = prev_node
        to_delete.prev = None
        to_delete.next = None
        self.size -= 1
    
    def _node_before(self, index: int) -> ListNode:
        node = self.dummy
        for _ in range(index):
            node = node.next
        return node

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)