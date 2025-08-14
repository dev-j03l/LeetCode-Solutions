class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque([(t, i) for i, t in enumerate(tickets)])
        seconds = 0

        while q:
            tickets_left, idx = q.popleft()
            tickets_left -= 1
            seconds += 1

            if tickets_left == 0:
                if idx == k:
                    return seconds
            else:
                q.append((tickets_left, idx))