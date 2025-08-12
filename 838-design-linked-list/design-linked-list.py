class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class MyLinkedList:
    def __init__(self):
        self.dummy = ListNode(0)
        self.size = 0

    def _node_before(self, index: int) -> ListNode:
        prev = self.dummy
        for _ in range(index):
            prev = prev.next
        return prev

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        return self._node_before(index).next.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0: index = 0
        if index > self.size: return
        prev = self._node_before(index)
        prev.next = ListNode(val, prev.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        prev = self._node_before(index)
        prev.next = prev.next.next
        self.size -= 1
