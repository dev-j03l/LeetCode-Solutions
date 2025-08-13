class Node:
    def __init__(self, url : str, next : Optional["Node"] = None, prev : Optional["Node"] = None):
        self.url = url
        self.next = next
        self.prev = prev
    
class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = self.currentPage = Node(homepage)
        

    def visit(self, url: str) -> None:
        self.currentPage.next = Node(url)
        tmp = self.currentPage.next
        tmp.prev = self.currentPage
        self.currentPage = tmp
        
    def back(self, steps: int) -> str:
        current = self.currentPage
        for _ in range(steps):
            if not current.prev: break
            current = current.prev

        self.currentPage = current
        return self.currentPage.url

    def forward(self, steps: int) -> str:
        current = self.currentPage
        for _ in range(steps):
            if not current.next: break
            current = current.next
        self.currentPage = current
        return self.currentPage.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)