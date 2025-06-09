import sys

class Student:
    def __init__(self, name, accepted, submit):
        self.name = name
        self.accepted = accepted
        self.submit = submit
    def __lt__(self, other):
        if self.accepted != other.accepted:
            return self.accepted > other.accepted
        elif self.submit != other.submit:
            return self.submit < other.submit
        else:
            return self.name < other.name
    def __str__(self):
        return f"{self.name} {self.accepted} {self.submit}"
    
n = (int(sys.stdin.readline()))
student = []
for _ in range(n):
    name = sys.stdin.readline().strip()
    accepted, submit = map (int, sys.stdin.readline().strip().split())
    student.append(Student(name, accepted, submit))
student.sort()
res = sorted(student, key = lambda s:(-s.accepted, s.submit, s.name))
for i in res:
    sys.stdout.write(str(i) + "\n")