class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant_q = deque()
        dire_q = deque()
        n =len(senate)

        for i, s in enumerate(senate):
            if s == "R":
                radiant_q.append(i)
            else:
                dire_q.append(i)
        
        while radiant_q and dire_q:
            dire = dire_q.popleft()
            radiant = radiant_q.popleft()
            if radiant < dire: radiant_q.append(radiant + n)
            else: dire_q.append(dire + n)

        return "Dire" if dire_q else "Radiant"
