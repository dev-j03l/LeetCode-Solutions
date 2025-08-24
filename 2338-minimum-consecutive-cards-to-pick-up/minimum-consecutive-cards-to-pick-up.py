class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        if len(set(cards)) == len(cards): return -1

        min_len = float('inf')
        L = 0
        tracker = set()
        for R in range(len(cards)):
            while cards[R] in tracker:
                min_len = min(min_len, R-L+1)
                if cards[L] in tracker: tracker.remove(cards[L])
                L += 1
            
            tracker.add(cards[R])
        
        return min_len

