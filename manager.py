class StudentManager:
    """Manages multiple Student objects."""

    def __init__(self):
        self.students = []

    def add_student(self, student):
        # Prevent duplicate student IDs.
        existing = self.search_student(student.student_id)
        if existing is not None:
            return False
        self.students.append(student)
        return True

    def remove_student(self, student_id):
        for index in range(len(self.students)):
            if self.students[index].student_id == int(student_id):
                del self.students[index]
                return True
        return False

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == int(student_id):
                return student
        return None

    def search_by_name(self, name):
        results = []
        search_text = name.lower()

        for student in self.students:
            if search_text in student.name.lower():
                results.append(student)

        return results

    def search_by_department(self, department):
        results = []
        search_text = department.lower()

        for student in self.students:
            if student.department.lower() == search_text:
                results.append(student)

        return results

    def search_by_average(self, minimum_average):
        results = []

        for student in self.students:
            if student.calculate_average() > float(minimum_average):
                results.append(student)

        return results

    def display_all_students(self):
        if len(self.students) == 0:
            return "No student records found."

        output = []
        for student in self.students:
            output.append(student.display_student())

        return "\n\n" + ("\n" + "-" * 40 + "\n").join(output)
