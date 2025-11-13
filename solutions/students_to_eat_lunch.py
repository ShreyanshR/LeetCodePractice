from collections import deque
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = 0
        students = deque(students)

        while sandwiches and counter < len(students):
            if sandwiches[0] == students[0]:
                sandwiches.pop(0)
                students.popleft()
                counter = 0
            else:
                x = students.popleft()
                students.append(x)
                counter += 1

        return counter


        
