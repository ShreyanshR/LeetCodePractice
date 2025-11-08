from typing import List
from collections import deque


class Solution:  
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0

        n = len(students)

        students = deque(students)

        while students and count < len(students):

            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.pop(0)
                
                print(students)
                print(sandwiches)
                count = 0
            else:
                students.append(students.popleft())
                count += 1


        return len(students)


if __name__ == "__main__":
    students = [1,1,0,0]
    sandwiches = [0,1,0,1]

    sol = Solution()

    sol.countStudents(students, sandwiches)

