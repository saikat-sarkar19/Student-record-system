# Student Record Management & Search System

## A. Title
Student Record Management & Search System

## B. Objective
The objective of this project is to develop a Python-based Student Record Management and Search System using Object-Oriented Programming (OOP). The project demonstrates classes, objects, constructors, attributes, instance methods, file handling, command-line arguments, and basic searching using loops and conditions.

## C. Features
- Add a new student
- Display student information
- Calculate total marks
- Calculate average marks
- Determine pass/fail status
- Update student marks
- Remove a student
- Search by Student ID
- Search by Name
- Search by Department
- Search students whose average marks are greater than a given value
- Read and write TXT files
- Read and write CSV files
- Read and write JSON files
- Run operations using command-line arguments

## D. Project Structure

```text
student-record-system/
├── main.py
├── student.py
├── manager.py
├── file_handler.py
├── data/
│   ├── students.txt
│   ├── students.csv
│   └── students.json
└── README.md
```

### Purpose of each Python file
- **main.py**: Command-line interface and program execution.
- **student.py**: Contains the `Student` class and student-related methods.
- **manager.py**: Contains the `StudentManager` class for managing multiple students and searching.
- **file_handler.py**: Contains methods for reading and writing TXT, CSV, and JSON files.

## E. Requirements
- Python 3.x
- No external packages are required.
- The project uses only Python built-in modules:
  - `argparse`
  - `csv`
  - `json`

Pandas and NumPy are not used.

## F. How to Run

Open a terminal inside the project folder.

### Display all students
```bash
python main.py --file data/students.csv --format csv --action display
```

### Search by Student ID
```bash
python main.py --file data/students.csv --format csv --action search-id --id 101
```

### Search by Name
```bash
python main.py --file data/students.csv --format csv --action search-name --name Rahul
```

### Search by Department
```bash
python main.py --file data/students.csv --format csv --action search-department --department "Computer Science"
```

### Search by Average Marks
```bash
python main.py --file data/students.csv --format csv --action search-average --average 75
```

### Add a Student
```bash
python main.py --file data/students.csv --format csv --action add --id 106 --name Riya --department Mathematics --semester 2 --subject1 80 --subject2 85 --subject3 90
```

### Update Student Marks
```bash
python main.py --file data/students.json --format json --action update-marks --id 101 --subject1 85 --subject2 88 --subject3 90
```

### Remove a Student
```bash
python main.py --file data/students.csv --format csv --action remove --id 105
```

### Save Records to Another Format
```bash
python main.py --file data/students.csv --format csv --action save --output data/output.json --output-format json
```

### TXT Example
```bash
python main.py --file data/students.txt --format txt --action display
```

### JSON Example
```bash
python main.py --file data/students.json --format json --action search-name --name Priya
```

## G. Input and Output

### Inputs
The program accepts:
- A file path through `--file`
- A file format through `--format`
- An operation through `--action`
- Additional values such as student ID, name, department, marks, or average depending on the selected action

### Required sample files
The `data` folder contains:
- `students.txt`
- `students.csv`
- `students.json`

Each sample file contains five student records.

### Output
The program displays results in the terminal. Add, remove, and update operations save changes back to the selected input file. The `save` action can create a separate output file.

### Example Output
```text
ID: 101
Name: Rahul
Department: Computer Science
Semester: 1
Subject 1: 78
Subject 2: 82
Subject 3: 69
Total: 229
Average: 76.33
Result: Pass
```

## H. OOP Concepts Used

### Classes
Two main classes are used:
- `Student`
- `StudentManager`

### Objects
Each student record is converted into a `Student` object.

### Constructors
The `Student` class uses `__init__()` to initialize student information. The `StudentManager` constructor initializes the student list.

### Attributes
Student attributes include:
- Student ID
- Name
- Department
- Semester
- Marks in three subjects

### Instance Methods
The `Student` class includes:
- `calculate_total()`
- `calculate_average()`
- `get_result()`
- `update_marks()`
- `display_student()`

The `StudentManager` class includes methods for adding, removing, displaying, and searching for students.

## I. File Handling Concepts Used

### TXT
TXT files are handled using:
- `open()`
- `readlines()`
- `write()`
- `with open(...)`
- File modes such as `r`, `w`, and `a`

### CSV
CSV files are handled using Python's built-in `csv` module:
- `csv.reader`
- `csv.writer`
- Header row handling

### JSON
JSON files are handled using Python's built-in `json` module:
- `json.load()`
- `json.dump()`
- Dictionaries and lists

## J. Searching Concepts Used

Searching is implemented using basic Python logic:
- `for` loops
- `if` conditions
- Comparisons
- String comparisons

The program supports:
- Search by Student ID
- Search by Name
- Search by Department
- Search by average marks greater than a specified value

No Pandas, NumPy, or specialized search libraries are used.

## K. Learning Outcome / Conclusion

This project provides practical experience with Python Object-Oriented Programming, file handling, command-line arguments, and basic searching. The main learning outcome is understanding the difference between an object representing one student and a class responsible for managing multiple students. The project also demonstrates how the same student data can be stored and retrieved using TXT, CSV, and JSON formats.
