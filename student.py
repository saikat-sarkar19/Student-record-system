class Student:
    """Represents one student's academic record."""

    PASS_MARK = 40

    def __init__(self, student_id, name, department, semester,
                 subject1, subject2, subject3):
        self.student_id = int(student_id)
        self.name = name
        self.department = department
        self.semester = int(semester)
        self.subject1 = float(subject1)
        self.subject2 = float(subject2)
        self.subject3 = float(subject3)

    def calculate_total(self):
        return self.subject1 + self.subject2 + self.subject3

    def calculate_average(self):
        return self.calculate_total() / 3

    def get_result(self):
        # A student passes only if every subject has the minimum pass mark.
        if (self.subject1 >= self.PASS_MARK and
                self.subject2 >= self.PASS_MARK and
                self.subject3 >= self.PASS_MARK):
            return "Pass"
        return "Fail"

    def update_marks(self, subject1, subject2, subject3):
        self.subject1 = float(subject1)
        self.subject2 = float(subject2)
        self.subject3 = float(subject3)

    def display_student(self):
        return (
            f"ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Department: {self.department}\n"
            f"Semester: {self.semester}\n"
            f"Subject 1: {self.subject1:g}\n"
            f"Subject 2: {self.subject2:g}\n"
            f"Subject 3: {self.subject3:g}\n"
            f"Total: {self.calculate_total():g}\n"
            f"Average: {self.calculate_average():.2f}\n"
            f"Result: {self.get_result()}"
        )

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "department": self.department,
            "semester": self.semester,
            "marks": {
                "subject1": self.subject1,
                "subject2": self.subject2,
                "subject3": self.subject3
            }
        }
