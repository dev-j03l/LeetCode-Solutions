class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant_q = deque()
        dire_q = deque()
        n = len(senate)

        for i, c in enumerate(senate):
            if c == "R":
                radiant_q.append(i)
            else:
                dire_q.append(i)
        
        while radiant_q and dire_q:
            r = radiant_q.popleft()
            d = dire_q.popleft()
            if r < d:
                radiant_q.append(r+n)
            else:
                dire_q.append(d+n)

        return "Dire" if dire_q else "Radiant" 

        