import csv
import json
from student import Student


class FileHandler:
    """Reads and writes student records in TXT, CSV, and JSON formats."""

    @staticmethod
    def load_txt(filename):
        students = []

        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()

                if line == "":
                    continue

                parts = line.split(",")

                if len(parts) != 7:
                    continue

                student = Student(
                    parts[0].strip(),
                    parts[1].strip(),
                    parts[2].strip(),
                    parts[3].strip(),
                    parts[4].strip(),
                    parts[5].strip(),
                    parts[6].strip()
                )
                students.append(student)

        return students

    @staticmethod
    def save_txt(filename, students):
        with open(filename, "w", encoding="utf-8") as file:
            for student in students:
                line = (
                    f"{student.student_id}, {student.name}, "
                    f"{student.department}, {student.semester}, "
                    f"{student.subject1:g}, {student.subject2:g}, "
                    f"{student.subject3:g}\n"
                )
                file.write(line)

    @staticmethod
    def append_txt(filename, student):
        with open(filename, "a", encoding="utf-8") as file:
            file.write(
                f"{student.student_id}, {student.name}, "
                f"{student.department}, {student.semester}, "
                f"{student.subject1:g}, {student.subject2:g}, "
                f"{student.subject3:g}\n"
            )

    @staticmethod
    def load_csv(filename):
        students = []

        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)

            # Skip the header row.
            next(reader, None)

            for row in reader:
                if len(row) != 7:
                    continue

                student = Student(
                    row[0], row[1], row[2], row[3],
                    row[4], row[5], row[6]
                )
                students.append(student)

        return students

    @staticmethod
    def save_csv(filename, students):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Student_ID", "Name", "Department", "Semester",
                "Subject1", "Subject2", "Subject3"
            ])

            for student in students:
                writer.writerow([
                    student.student_id,
                    student.name,
                    student.department,
                    student.semester,
                    student.subject1,
                    student.subject2,
                    student.subject3
                ])

    @staticmethod
    def load_json(filename):
        students = []

        with open(filename, "r", encoding="utf-8") as file:
            records = json.load(file)

        for record in records:
            marks = record["marks"]

            student = Student(
                record["student_id"],
                record["name"],
                record["department"],
                record["semester"],
                marks["subject1"],
                marks["subject2"],
                marks["subject3"]
            )
            students.append(student)

        return students

    @staticmethod
    def save_json(filename, students):
        records = []

        for student in students:
            records.append(student.to_dict())

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(records, file, indent=4)

    @staticmethod
    def load_file(filename, file_format):
        file_format = file_format.lower()

        if file_format == "txt":
            return FileHandler.load_txt(filename)
        if file_format == "csv":
            return FileHandler.load_csv(filename)
        if file_format == "json":
            return FileHandler.load_json(filename)

        raise ValueError("Unsupported format. Use txt, csv, or json.")

    @staticmethod
    def save_file(filename, file_format, students):
        file_format = file_format.lower()

        if file_format == "txt":
            FileHandler.save_txt(filename, students)
        elif file_format == "csv":
            FileHandler.save_csv(filename, students)
        elif file_format == "json":
            FileHandler.save_json(filename, students)
        else:
            raise ValueError("Unsupported format. Use txt, csv, or json.")
