class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        start_time = 0
        arr = [0] * n
        for task in logs:
            arr[task[0]] = max(task[1] - start_time, arr[task[0]])
            start_time = task[1]
        
        max_task =  -1
        max_employee = -1
        for i, taskLength in enumerate(arr):
            if taskLength > max_task:
                max_employee = i
                max_task = taskLength
        
        return max_employee
            