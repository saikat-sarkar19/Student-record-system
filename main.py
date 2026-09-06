import argparse
from student import Student
from manager import StudentManager
from file_handler import FileHandler


def print_students(students):
    if len(students) == 0:
        print("No matching student records found.")
        return

    for student in students:
        print(student.display_student())
        print("-" * 40)


def create_parser():
    parser = argparse.ArgumentParser(
        description="Student Record Management and Search System"
    )

    parser.add_argument("--file", required=True,
                        help="Input file containing student records")
    parser.add_argument("--format", required=True,
                        choices=["txt", "csv", "json"],
                        help="Format of the input file")
    parser.add_argument("--action", required=True,
                        choices=[
                            "display", "search-id", "search-name",
                            "search-department", "search-average",
                            "add", "remove", "update-marks", "save"
                        ],
                        help="Operation to perform")

    parser.add_argument("--id", type=int, help="Student ID")
    parser.add_argument("--name", help="Student name")
    parser.add_argument("--department", help="Department name")
    parser.add_argument("--semester", type=int, help="Semester number")
    parser.add_argument("--subject1", type=float, help="Marks in subject 1")
    parser.add_argument("--subject2", type=float, help="Marks in subject 2")
    parser.add_argument("--subject3", type=float, help="Marks in subject 3")
    parser.add_argument("--average", type=float,
                        help="Minimum average for condition search")
    parser.add_argument("--output", help="Output file for save operation")
    parser.add_argument("--output-format",
                        choices=["txt", "csv", "json"],
                        help="Format of the output file")

    return parser


def load_manager(filename, file_format):
    manager = StudentManager()
    students = FileHandler.load_file(filename, file_format)

    for student in students:
        manager.add_student(student)

    return manager


def require_arguments(parser, args, names):
    for name in names:
        if getattr(args, name) is None:
            parser.error(f"--{name.replace('_', '-')} is required for this action")


def main():
    parser = create_parser()
    args = parser.parse_args()

    try:
        manager = load_manager(args.file, args.format)
    except FileNotFoundError:
        print(f"Error: File not found: {args.file}")
        return
    except (ValueError, KeyError, TypeError) as error:
        print(f"Error while reading file: {error}")
        return

    if args.action == "display":
        print(manager.display_all_students())

    elif args.action == "search-id":
        require_arguments(parser, args, ["id"])
        student = manager.search_student(args.id)

        if student is None:
            print("Student not found.")
        else:
            print(student.display_student())

    elif args.action == "search-name":
        require_arguments(parser, args, ["name"])
        print_students(manager.search_by_name(args.name))

    elif args.action == "search-department":
        require_arguments(parser, args, ["department"])
        print_students(manager.search_by_department(args.department))

    elif args.action == "search-average":
        require_arguments(parser, args, ["average"])
        print_students(manager.search_by_average(args.average))

    elif args.action == "add":
        require_arguments(
            parser, args,
            ["id", "name", "department", "semester",
             "subject1", "subject2", "subject3"]
        )

        student = Student(
            args.id, args.name, args.department, args.semester,
            args.subject1, args.subject2, args.subject3
        )

        if manager.add_student(student):
            FileHandler.save_file(args.file, args.format, manager.students)
            print("Student added successfully.")
        else:
            print("A student with this ID already exists.")

    elif args.action == "remove":
        require_arguments(parser, args, ["id"])

        if manager.remove_student(args.id):
            FileHandler.save_file(args.file, args.format, manager.students)
            print("Student removed successfully.")
        else:
            print("Student not found.")

    elif args.action == "update-marks":
        require_arguments(
            parser, args,
            ["id", "subject1", "subject2", "subject3"]
        )

        student = manager.search_student(args.id)

        if student is None:
            print("Student not found.")
        else:
            student.update_marks(
                args.subject1, args.subject2, args.subject3
            )
            FileHandler.save_file(args.file, args.format, manager.students)
            print("Student marks updated successfully.")

    elif args.action == "save":
        require_arguments(parser, args, ["output", "output_format"])

        try:
            FileHandler.save_file(
                args.output, args.output_format, manager.students
            )
            print(f"Records saved successfully to {args.output}")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
