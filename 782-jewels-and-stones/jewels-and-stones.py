class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_map = {}
        for jewel in jewels:
            jewels_map[jewel] = 1
        
        jewel_count = 0
        for stone in stones:
            if stone in jewels_map:
                jewel_count += 1
        
        return jewel_count
