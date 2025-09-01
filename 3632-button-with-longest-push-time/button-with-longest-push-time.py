from typing import List

class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        prev_time = 0
        max_ind = -1
        max_time = -1

        for i in range(len(events)):
            duration = events[i][1] - prev_time
            if duration > max_time or (duration == max_time and events[i][0] < max_ind):
                max_ind = events[i][0]
                max_time = duration
            prev_time = events[i][1]  # update for next loop

        return max_ind
