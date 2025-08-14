class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        if len(students) == 0: return 0
        student_q = deque()
        # Add all our students to the queue
        for student in students:
            student_q.append(student)
        
        size_q = len(students)
        top = 0

        while student_q and size_q:
            first = student_q.popleft()
            if first == sandwiches[top]:
                top += 1
                size_q = len(student_q)
            else:
                size_q -= 1
                student_q.append(first)
        return len(student_q)
        