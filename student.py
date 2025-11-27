#Maintaining a Student Result System with Sorting & Searching
#Write a Python program to maintain a student result system with the following operations:
#Add a student (ID, Name, Marks)
#Search for a student by ID
#Sort students by marks
#Count number of students who failed (marks < 40)
#Display the top 5 students based on marks

class StudentSystem:
    def __init__(self):
        self.students = []   # list of dicts

    def add_student(self, sid, name, marks):
        self.students.append({"id": sid, "name": name, "marks": marks})

    def search_by_id(self, sid):
        for s in self.students:
            if s["id"] == sid:
                return s
        return None

    def sort_by_marks(self):
        return sorted(self.students, key=lambda x: x["marks"])

    def count_fail(self):
        return sum(1 for s in self.students if s["marks"] < 40)

    def top_5(self):
        return sorted(self.students, key=lambda x: x["marks"], reverse=True)[:5]


s = StudentSystem()

s.add_student(1, "ubaid", 85)
s.add_student(2, "kamran", 35)
s.add_student(3, "sahil", 90)
s.add_student(4, "mohsin", 55)
s.add_student(5, "faheem", 28)

print("Search ID 3:", s.search_by_id(3))
print("Sorted by marks:", s.sort_by_marks())
print("Failures:", s.count_fail())
print("Top 5:", s.top_5())
