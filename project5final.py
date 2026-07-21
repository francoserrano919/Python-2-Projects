"""
script: project5final.py
action: a. Defines classes Person, Employee, Student with validation and methods.
        b. Functions to load data from text files into these classes.
        c. Functions to display various reports based on the loaded data.
author: Franco Xavier Serrano
date: 12/16/2025
"""
from __future__ import annotations
import re
from abc import ABC
from datetime import date
from pathlib import Path


# Abstract Base Class: Person
class Person(ABC):
    """
    Class Person: Abstract base class for people with common attributes.

    action: Represents a person with first name, last name, ID number,
            email address, and phone number.
    input: firstName (str): First name of the person.
            lastName (str): Last name of the person.
            idNumber (int): ID number of the person.
            emailAddress (str): Email address of the person.
            phoneNumber (str): Phone number of the person.
    output: None
    return: None
    """
   
    # Provide a concrete default that subclasses may override.
    def kind(self) -> str:
        return self.__class__.__name__

    def __init__(self, firstName: str, lastName: str, idNumber: int,
                 emailAddress: str, phoneNumber: str) -> None:
        
        # Validate names
        firstName = str(firstName).strip()
        lastName = str(lastName).strip()
        if not firstName or not lastName:
            raise ValueError("First Name and Last Name must be non-empty.")

        # Validate idNumber: 4 digits
        try:
            idNumber = int(idNumber)
        except (TypeError, ValueError):
            raise ValueError("ID Number must be a 4-digit integer.") from None
        if not (1000 <= idNumber <= 9999):
            raise ValueError("ID Number must be a 4-digit integer (1000-9999).")

        # Validate phone (###-###-####) and email
        phoneNumber = str(phoneNumber).strip()
        if not re.fullmatch(r"\d{3}-\d{3}-\d{4}", phoneNumber):
            raise ValueError("Phone Number must be in the format ###-###-####.")
        emailAddress = str(emailAddress).strip()
        if emailAddress and "@" not in emailAddress:
            raise ValueError("Email Address must contain '@' when provided.")

        # Set attributes
        self._firstName = firstName
        self._lastName = lastName
        self._idNumber = idNumber
        self._emailAddress = emailAddress
        self._phoneNumber = phoneNumber

    # Properties with validation
    @property
    def firstName(self) -> str:
        return self._firstName

    # Last Name property
    @property
    def lastName(self) -> str:
        return self._lastName

    # idNumber to be read-only
    @property
    def idNumber(self) -> int:
        return self._idNumber

    # Email property
    @property
    def emailAddress(self) -> str:
        return self._emailAddress

    # Setter with validation
    @emailAddress.setter
    def emailAddress(self, value: str) -> None:
        """Validate email format when setting."""
        value = str(value).strip()
        if value and "@" not in value:
            raise ValueError("Email Address must contain '@' when provided.")
        self._emailAddress = value

    # Phone Number property
    @property
    def phoneNumber(self) -> str:
        return self._phoneNumber

    # Setter with validation
    @phoneNumber.setter
    def phoneNumber(self, value: str) -> None:
        value = str(value).strip()
        if not re.fullmatch(r"\d{3}-\d{3}-\d{4}", value):
            raise ValueError("Phone Number must be in the format ###-###-####.")
        self._phoneNumber = value

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(firstName={self.firstName!r}, "
                f"lastName={self.lastName!r}, idNumber={self.idNumber!r})")

    def __str__(self) -> str:
        return f"{self.lastName}, {self.firstName} ({self.idNumber})"


# Employee Class
class Employee(Person):
    """
    Class Employee: Concrete subclass of Person with employment-specific fields.
    action: Represents an employee with hire date, role, classification, and salary.
    input: firstName (str): First name of the employee.
            lastName (str): Last name of the employee.
            idNumber (int): ID number of the employee.
            emailAddress (str): Email address of the employee.
            phoneNumber (str): Phone number of the employee.
            hireYear (int): Year of hire.
            hireMonth (int): Month of hire.
            hireDay (int): Day of hire.
            rolePerson (str): Role of the employee.
            classificationPerson (str): Classification of the employee.
            annualSalary (float): Annual salary of the employee.
    output: None
    return: None
    """

    # Dictionaries for role and classification
    roleDictionary = {"001": "Staff", "002": "Faculty"}
    classificationDictionary = {"001": "Full", "002": "Part"}

    # Provide a concrete default that subclasses may override.
    def kind(self) -> str:
        return "Employee"

    def __init__(self, firstName: str, lastName: str, idNumber: int,
                 emailAddress: str, phoneNumber: str,
                 hireYear: int, hireMonth: int, hireDay: int,
                 rolePerson: str, classificationPerson: str,
                 annualSalary: float) -> None:
        super().__init__(firstName, lastName, idNumber, emailAddress, phoneNumber)

        # Hire date
        try:
            self._hireDate = date(int(hireYear), int(hireMonth), int(hireDay))
        except Exception as e:
            raise ValueError(f"Hire Date must be a valid date (MM/DD/YYYY parts): {e}")

        # Role and classification keys
        if rolePerson not in Employee.roleDictionary:
            raise ValueError("Role Person must be a key in roleDictionary (e.g., '001').")
        if classificationPerson not in Employee.classificationDictionary:
            raise ValueError("Classification must be a key in classificationDictionary (e.g., '001').")

        self._rolePerson = rolePerson
        self._classificationPerson = classificationPerson

        # Salary with validation
        try:
            annualSalary = float(annualSalary)
        except (TypeError, ValueError):
            raise ValueError("Annual salary must be numeric.") from None
        if annualSalary < 0:
            raise ValueError("Annual salary must be non‑negative.")
        self._annualSalary = round(annualSalary, 2)

    # Properties with validation
    @property
    def hireDate(self) -> date:
        return self._hireDate

    # Role property
    @property
    def rolePerson(self) -> str:
        return self._rolePerson

    # Setter with validation
    @rolePerson.setter
    def rolePerson(self, key: str) -> None:
        if key not in Employee.roleDictionary:
            raise ValueError("Role Person must be a key in roleDictionary (e.g., '001').")
        self._rolePerson = key

    # Classification property
    @property
    def classificationPerson(self) -> str:
        return self._classificationPerson

    # Setter with validation
    @classificationPerson.setter
    def classificationPerson(self, key: str) -> None:
        if key not in Employee.classificationDictionary:
            raise ValueError("Classification must be a key in classificationDictionary (e.g., '001').")
        self._classificationPerson = key

    # Annual Salary property
    @property
    def annualSalary(self) -> float:
        return self._annualSalary

    # Setter with validation
    @annualSalary.setter
    def annualSalary(self, value: float) -> None:
        try:
            value = float(value)
        except (TypeError, ValueError):
            raise ValueError("Annual salary must be numeric.") from None
        if value < 0:
            raise ValueError("Annual salary must be non‑negative.")
        self._annualSalary = round(value, 2)

    # String representation
    def __repr__(self) -> str:
        return (f"Employee({self.lastName}, {self.firstName}, id={self.idNumber}, "
                f"role={self._rolePerson}, class={self._classificationPerson}, salary={self._annualSalary:.2f})")

    def __str__(self) -> str:
        return f"{self.lastName}, {self.firstName} | {self.idNumber} | {self.emailAddress} | {self.phoneNumber}"


# Student Class
class Student(Person):
    """Class Student: Concrete Student subclass with academic scores.
    action: Represents a student with course scores.
    input: firstName (str): First name of the student.
           lastName (str): Last name of the student.
           idNumber (int): ID number of the student.
           emailAddress (str): Email address of the student.
           phoneNumber (str): Phone number of the student.
    output: None
    return: None
    """

    # Class variable: list of course names 
    courseNameList = [
        "Art",
        "Latin",
        "Greek",
        "Mathematics",
        "Science",
    ]

    def __init__(self, firstName: str, lastName: str, idNumber: int,
                 emailAddress: str, phoneNumber: str) -> None:
        super().__init__(firstName, lastName, idNumber, emailAddress, phoneNumber)
        # Instance dictionary {courseName: score}
        self.coursesStudentDict: dict[str, int] = {}

    def kind(self) -> str:
        return "Student"

    def add_course_score(self, course: str, score: int) -> None:
        """
        Add or update a single course score with validation.
        action: Validates and adds/updates a course score.
        input: course (str): Name of the course.
               score (int): Score for the course (0-100).
        output: None
        return: None
        """
        course = str(course).strip()
        if course not in Student.courseNameList:
            raise ValueError(f"Course '{course}' is not in courseNameList.")
        try:
            score_int = int(score)
        except (TypeError, ValueError):
            raise ValueError("Score must be an integer.") from None
        if not (0 <= score_int <= 100):
            raise ValueError("Score must be between 0 and 100.")
        self.coursesStudentDict[course] = score_int

    # Method to get academic record
    def getStudentAcademics(self) -> str:
        """
        Return comma-separated academic record for this student.
        
        action: Generates a string of the student's academic record.
        input: None
        output: None
        return: str - Comma-separated academic record.
        """
        # Order the same as example output
        ordered_courses = ["Art", "Greek", "Latin", "Science", "Mathematics"]
        scores = [str(self.coursesStudentDict.get(c, 0)) for c in ordered_courses]
        parts = [self.lastName, self.firstName, str(self.idNumber), *scores]
        return ",".join(parts)

    # Method to get high score
    def getHighScore(self) -> int:
        """
        Return the highest score for this student.

        action: Finds the highest score among the student's courses.
        input: None
        output: None
        return: int - Highest score.
        """
        if not self.coursesStudentDict:
            return 0
        return max(self.coursesStudentDict.values())

    # Method to get low score
    def getLowScore(self) -> int:
        """
        Return the lowest score for this student.
        
        action: Finds the lowest score among the student's courses.
        input: None
        output: None
        return: int - Lowest score.
        """
        if not self.coursesStudentDict:
            return 0
        return min(self.coursesStudentDict.values())

    # Method to get average score
    def getAverageScore(self) -> float:
        """
        Return the average score for this student.

        action: Calculates the average score among the student's courses.
        input: None
        output: None
        return: float - Average score.
        """
        if not self.coursesStudentDict:
            return 0.0
        return sum(self.coursesStudentDict.values()) / len(self.coursesStudentDict)

    # Method to get letter grade
    def getGrade(self) -> str:
        """
        Return letter grade based on Pima grading scale.

        action: Determines the letter grade from the average score.
        input: None
        output: None
        return: str - Letter grade.
        """
        avg = self.getAverageScore()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

    def __repr__(self) -> str:
        return f"Student({self.lastName}, {self.firstName}, id={self.idNumber})"

    def __str__(self) -> str:
        # Explicit __str__ to satisfy rubric, using Person behavior
        return super().__str__()


# Helpers to map labels to keys
def label_to_key(mapping: dict, label: str) -> str | None:
    """
    Map a label (like 'Full', 'Staff') to its key ('001'/'002').

    action: Converts a human-readable label to its corresponding key in a mapping.
    input: mapping (dict): Dictionary mapping keys to labels.
           label (str): Human-readable label to map.
    output: None
    return: str | None - Corresponding key if found, else None.
    """
    if not label:
        return None
    label_norm = str(label).strip().lower()

    # Direct value match
    for k, v in mapping.items():
        if str(v).strip().lower() == label_norm:
            return k

    # Common synonyms to keys in case of no direct match
    synonyms = {
        "full-time": "001", "full time": "001", "full": "001",
        "part-time": "002", "part time": "002", "part": "002",
        "staff": "001" if "Staff" in mapping.values() else None,
        "faculty": "002" if "Faculty" in mapping.values() else None,
    }
    chosen = synonyms.get(label_norm)
    if chosen and chosen in mapping:
        return chosen
    return None

# Functions to load data from files
def _open_data_file(path: str | Path) -> Path:
    """
    Locate a data file either in CWD or ~/Downloads.
    
    action: Checks for the existence of a file in the current working directory
    input: path (str | Path): Relative or absolute path to the data file.
    output: None
    return: Path - Path to the found data file.
    """
    p = Path(path)
    if p.exists():
        return p
    fallback = Path.home() / 'Downloads' / p.name
    if fallback.exists():
        return fallback
    raise FileNotFoundError(f"Data file not found at {p} or {fallback}.")

# Function to split columns
def _split_columns(line: str, expected: int) -> list[str] | None:
    """
    Split a data line trying different whitespace patterns.
    
    action: Attempts to split a line into columns using tabs or spaces.
    input: line (str): The line to split.
           expected (int): Minimum expected number of columns.
    output: None
    return: list[str] | None - List of column values if successful, else None.
    """
    line = line.strip()
    if not line:
        return None

    for pattern in (r"\t+", r"\s{2,}", r"\s+"):
        parts = re.split(pattern, line)
        if len(parts) >= expected:
            return parts
    return None

# Function to get employees from file
def getEmployees(file_path: str = 'employees.txt') -> list[Employee]:
    """
    Load employees from a text file and return a list of Employee objects.
    
    action: Reads employee data from a file and creates Employee objects.
    input: file_path (str): Path to the employee data file.
    output: None
    return: list[Employee] - List of Employee objects.
    """
    employeeList: list[Employee] = []
    print("\nAdding employees…\n")
    try:
        p = _open_data_file(file_path)
    except FileNotFoundError:
        print(f"Error: '{file_path}' was not found in CWD or ~/Downloads.")
        return employeeList

    # Open and read file
    with p.open('r', encoding='utf-8') as f:
        header_skipped = False
        for line in f:
            if not header_skipped:
                header_skipped = True
                continue
            cols = _split_columns(line, 9)
            if not cols:
                continue

            # Expected layout from employees.txt
            lastName = cols[0]
            firstName = cols[1]
            emp_id = cols[2]
            email = cols[3]
            phone_raw = cols[4]
            hireDate_str = cols[5]
            classification_label = cols[6]
            role_label = cols[7]
            salary = cols[8]

            # Normalize phone to ###-###-####
            phone_digits = re.sub(r"\D", "", phone_raw)
            if len(phone_digits) == 10:
                phone = f"{phone_digits[0:3]}-{phone_digits[3:6]}-{phone_digits[6:]}"
            else:
                phone = "000-000-0000"

            # Parse hire date M/D/YYYY
            try:
                m_s, d_s, y_s = hireDate_str.split('/')
            except ValueError:
                print(f"Skipping employee with bad date: {line.strip()}")
                continue

            role_key = label_to_key(Employee.roleDictionary, role_label) or '001'
            class_key = label_to_key(Employee.classificationDictionary, classification_label) or '001'

            # Try to create Employee object
            try:
                emp = Employee(firstName, lastName, int(emp_id), email, phone,
                               int(y_s), int(m_s), int(d_s),
                               role_key, class_key, float(salary))
                employeeList.append(emp)
                print(f"Added employee {firstName} {lastName}…")
            except Exception as e:
                print(f"Skipping employee record due to error: {e}")
    return employeeList

# Function to get students from file
def getStudents(file_path: str = 'students.txt') -> list[Student]:
    """
    Load students from a text file and return a list of Student objects.
    
    action: Reads student data from a file and creates Student objects.
    input: file_path (str): Path to the student data file.
    output: None
    return: list[Student] - List of Student objects.
    """
    studentList: list[Student] = []
    print("\nAdding students…\n")
    try:
        p = _open_data_file(file_path)
    except FileNotFoundError:
        print(f"Error: '{file_path}' was not found in CWD or ~/Downloads.")
        return studentList

    # Open and read file
    with p.open('r', encoding='utf-8') as f:
        header_skipped = False
        for line in f:
            if not header_skipped:
                header_skipped = True
                continue
            cols = _split_columns(line, 5)
            if not cols:
                continue
            lastName = cols[0]
            firstName = cols[1]
            stud_id = cols[2]
            email = cols[3]
            phone_raw = cols[4]

            # Normalize phone to ###-###-####
            phone_digits = re.sub(r"\D", "", phone_raw)
            if len(phone_digits) == 10:
                phone = f"{phone_digits[0:3]}-{phone_digits[3:6]}-{phone_digits[6:]}"
            else:
                phone = "000-000-0000"

            # Try to create Student object
            try:
                s = Student(firstName, lastName, int(stud_id), email, phone)
                studentList.append(s)
                print(f"Added student {firstName} {lastName}…")
            except Exception as e:
                print(f"Skipping student record due to error: {e}")
    return studentList

# Helper to find student by ID
def getStudentById(studentList: list[Student], stud_id: int) -> Student | None:
    """
    Helper to locate a Student by ID in the list.
    action: Searches for a Student object by its ID number.
    input: studentList (list[Student]): List of Student objects.
           stud_id (int): ID number to search for.
    output: None
    return: Student | None - Found Student object or None if not found."""
    for s in studentList:
        if s.idNumber == stud_id:
            return s
    return None

# Function to get student scores from file
def getStudentScores(studentList: list[Student], file_path: str = 'scores.txt') -> None:
    """
    Read scores.txt and add scores into each Student object's dictionary.
    
    action: Reads scores from a file and updates Student objects with their scores.
    input: studentList (list[Student]): List of Student objects to update.
           file_path (str): Path to the scores data file.
    output: None
    return: None
    """
    print("\nAdding student scores…\n")
    try:
        p = _open_data_file(file_path)
    except FileNotFoundError:
        print(f"Error: '{file_path}' was not found in CWD or ~/Downloads.")
        return

    # Open and read file
    with p.open('r', encoding='utf-8') as f:
        header_skipped = False

        # Determine order of courses from header so we align correctly
        header_courses: list[str] = []
        for line in f:
            if not header_skipped:
                header_skipped = True
                header_parts = _split_columns(line, 2) or []

                # First column is ID, rest are course names
                if len(header_parts) >= 2:
                    header_courses = header_parts[1:]
                continue
            
            # Process score lines
            cols = _split_columns(line, 2)
            if not cols:
                continue
            stud_id_str = cols[0]

            # Find student by ID
            try:
                stud_id = int(stud_id_str)
            except ValueError:
                print(f"Skipping scores line with bad id: {line.strip()}")
                continue

            student = getStudentById(studentList, stud_id)
            if not student:
                print(f"No matching student for ID {stud_id}; skipping scores.")
                continue

            score_values = cols[1:]

            # Zip header courses with scores (extra scores ignored)
            for course, score_str in zip(header_courses, score_values):
                course = course.strip()
                if course not in Student.courseNameList:
                    # Skip unknown courses like project requirements states
                    continue
                if score_str == "":
                    continue
                try:
                    student.add_course_score(course, int(score_str))
                except Exception as e:
                    print(f"Could not add score for {student.firstName} {student.lastName}: {e}")

            print(f"Added scores for {student.firstName} {student.lastName}…")


# Function to display reports
def displayEmployeeEmploymentInformation(employeeList: list[Employee]) -> None:
    """
    Display employment information for all employees.
    
    action: Prints a formatted report of employee employment information.
    input: employeeList (list[Employee]): List of Employee objects.
    output: None
    return: None
    """
    print("\n\t\t\tEmployee Employment Information\n")
    print(f"{'LastName':<12}{'FirstName':<12}{'ID':<6}{'Email':<30}{'Phone':<14}{'HireDate':<12}{'Classification':<15}{'Role':<10}{'Salary':>12}")
    for e in employeeList:
        hire_str = f"{e.hireDate.month}/{e.hireDate.day}/{e.hireDate.year}"
        classification = Employee.classificationDictionary.get(e.classificationPerson, '?')
        role = Employee.roleDictionary.get(e.rolePerson, '?')
        print(f"{e.lastName:<12}{e.firstName:<12}{e.idNumber:<6}{e.emailAddress:<30}{e.phoneNumber:<14}{hire_str:<12}{classification:<15}{role:<10}{e.annualSalary:>12.2f}")

# Function to display contact information
def displayEmployeeContactInformation(employeeList: list[Employee]) -> None:
    """
    Display contact information for all employees.

    action: Prints a formatted report of employee contact information.
    input: employeeList (list[Employee]): List of Employee objects.
    output: None
    return: None
    """
    print("\n\t\tEmployee Contact Information\n")
    print(f"{'LastName':<12}{'FirstName':<12}{'ID':<6}{'Email':<30}{'Phone':<14}")
    for e in employeeList:
        print(f"{e.lastName:<12}{e.firstName:<12}{e.idNumber:<6}{e.emailAddress:<30}{e.phoneNumber:<14}")

# Function to display student contact information
def displayStudentContactInformation(studentList: list[Student]) -> None:
    """
    Display contact information for all students.

    action: Prints a formatted report of student contact information.
    input: studentList (list[Student]): List of Student objects.
    output: None
    return: None
    """
    print("\n\t\tStudent Contact Information\n")
    print(f"{'LastName':<12}{'FirstName':<12}{'ID':<6}{'Email':<30}{'Phone':<14}")
    for s in studentList:
        print(f"{s.lastName:<12}{s.firstName:<12}{s.idNumber:<6}{s.emailAddress:<30}{s.phoneNumber:<14}")

# Function to display all person contact information
def displayAllPersonContactInformation(employeeList: list[Employee], studentList: list[Student]) -> None:
    """
    Display contact information for all employees and students.

    action: Prints a formatted report of all person contact information.
    input: employeeList (list[Employee]): List of Employee objects.
           studentList (list[Student]): List of Student objects.
    output: None
    return: None
    """
    print("\n\t\tAll Person Contact Information\n")
    print(f"{'LastName':<12}{'FirstName':<12}{'ID':<6}{'Email':<30}{'Phone':<14}")
    personList: list[Person] = []
    personList.extend(employeeList)
    personList.extend(studentList)
    for p in personList:
        print(f"{p.lastName:<12}{p.firstName:<12}{p.idNumber:<6}{p.emailAddress:<30}{p.phoneNumber:<14}")

# Function to get student academic report
def getStudentAcademicReport(student: Student) -> dict:
    """
    Get academic report for a single Student object.

    action: Compiles a dictionary of academic report fields for a student.
    input: student (Student): The Student object to report on.
    output: None
    return: dict - Dictionary containing academic report fields.
    """
    ordered_courses = ["Art", "Greek", "Latin", "Science", "Mathematics"]
    scores = {c: student.coursesStudentDict.get(c, 0) for c in ordered_courses}
    
    return {
        'lastName': student.lastName,
        'firstName': student.firstName,
        'id': student.idNumber,
        'Art': scores['Art'],
        'Greek': scores['Greek'],
        'Latin': scores['Latin'],
        'Science': scores['Science'],
        'Mathematics': scores['Mathematics'],
        'high': student.getHighScore(),
        'low': student.getLowScore(),
        'average': round(student.getAverageScore(), 1),
        'grade': student.getGrade()
    }

# Function to display full student academic report
def displayFullStudentAcademicReport(studentList: list[Student]) -> None:
    """
    Display the Full Academic Report for all students (menu option 6).
    
    action: Prints a formatted report of all students' academic records.
    input: studentList (list[Student]): List of Student objects.
    output: None
    return: None
    """
    print("\n\t\t\t\tFull Academic Report\n")
    
    # Print header
    header = f"{'LastName':<12}{'FirstName':<12}{'ID':<6}{'Art':>6}{'Greek':>8}{'Latin':>8}{'Science':>10}{'Math':>8}{'High':>8}{'Low':>8}{'Average':>10}{'Grade':>8}"
    print(header)
    
    # Collect course scores for summary calculations
    course_scores = {'Art': [], 'Greek': [], 'Latin': [], 'Science': [], 'Mathematics': []}
    
    # Print each student's report
    for s in studentList:
        report = getStudentAcademicReport(s)
        print(f"{report['lastName']:<12}{report['firstName']:<12}{report['id']:<6}"
              f"{report['Art']:>6}{report['Greek']:>8}{report['Latin']:>8}"
              f"{report['Science']:>10}{report['Mathematics']:>8}"
              f"{report['high']:>8}{report['low']:>8}{report['average']:>10}{report['grade']:>8}")
        
        # Collect scores for course summaries
        for course in course_scores:
            course_scores[course].append(report[course])
    
    # Print blank line before summary
    print()
    
    # Calculate and print course summaries (High, Low, Average)
    highs = {c: max(scores) for c, scores in course_scores.items()}
    lows = {c: min(scores) for c, scores in course_scores.items()}
    avgs = {c: round(sum(scores) / len(scores), 1) for c, scores in course_scores.items()}
    
    print(f"{'High':<12}{'':<12}{'':<6}{highs['Art']:>6}{highs['Greek']:>8}{highs['Latin']:>8}{highs['Science']:>10}{highs['Mathematics']:>8}")
    print(f"{'Low':<12}{'':<12}{'':<6}{lows['Art']:>6}{lows['Greek']:>8}{lows['Latin']:>8}{lows['Science']:>10}{lows['Mathematics']:>8}")
    print(f"{'Average':<12}{'':<12}{'':<6}{avgs['Art']:>6}{avgs['Greek']:>8}{avgs['Latin']:>8}{avgs['Science']:>10}{avgs['Mathematics']:>8}")

# Function to look up student academic record
def lookUpStudentAcademicRecord(studentList: list[Student]) -> None:
    """
    Look up and display academic report for one student (menu option 7).
    
    action: Prompts for a student ID and displays their academic report.
    input: studentList (list[Student]): List of Student objects.
    output: None
    return: None
    """
    while True:
        print("\nPlease enter the ID of the student")
        user_input = input("\n>> ").strip()
        
        # Check for quit
        if user_input == '-1':
            return
        
        # Validate input is a number
        try:
            stud_id = int(user_input)
        except ValueError:
            print("\nThat is not a valid ID. Please try again or enter -1 to quit.")
            continue
        
        # Find the student
        student = getStudentById(studentList, stud_id)
        
        if student is None:
            print("\nThat is not an ID we have on record. Please try again or enter -1 to quit.")
            continue
        
        # Display the student's report
        print("\n\t\t\t\tIndividual Student Report\n")
        header = f"{'LastName':<12}{'FirstName':<12}{'ID':<6}{'Art':>6}{'Greek':>8}{'Latin':>8}{'Science':>10}{'Math':>8}{'High':>8}{'Low':>8}{'Average':>10}{'Grade':>8}"
        print(header)
        
        report = getStudentAcademicReport(student)
        print(f"{report['lastName']:<12}{report['firstName']:<12}{report['id']:<6}"
              f"{report['Art']:>6}{report['Greek']:>8}{report['Latin']:>8}"
              f"{report['Science']:>10}{report['Mathematics']:>8}"
              f"{report['high']:>8}{report['low']:>8}{report['average']:>10}{report['grade']:>8}")
        return

# Function to get honor roll students
def getHonorRoll(studentList: list[Student]) -> None:
    """
    Display students who made the Honor Roll - grade of A (menu option 8).
    
    action: Prints a formatted report of students with an 'A' grade.
    input: studentList (list[Student]): List of Student objects.
    output: None
    return: None
    """
    print("\n\t\t\t\tHonor Roll Report\n")
    
    # Print header
    header = f"{'LastName':<12}{'FirstName':<12}{'ID':<6}{'Art':>6}{'Greek':>8}{'Latin':>8}{'Science':>10}{'Math':>8}{'High':>8}{'Low':>8}{'Average':>10}{'Grade':>8}"
    print(header)
    
    # Print each student with an A grade
    for s in studentList:
        report = getStudentAcademicReport(s)
        if report['grade'] == 'A':
            print(f"{report['lastName']:<12}{report['firstName']:<12}{report['id']:<6}"
                  f"{report['Art']:>6}{report['Greek']:>8}{report['Latin']:>8}"
                  f"{report['Science']:>10}{report['Mathematics']:>8}"
                  f"{report['high']:>8}{report['low']:>8}{report['average']:>10}{report['grade']:>8}")


# Sorting functions for Project 5
def sortStudentListByLastName(studentList: list[Student]) -> list[Student]:
    """
    Sort the student list by last name alphabetically.
    
    action: Sorts a list of Student objects by their lastName attribute.
    input: studentList (list[Student]): List of Student objects to sort.
    output: None
    return: list[Student] - Sorted list of Student objects.
    """
    return sorted(studentList, key=lambda student: student.lastName.lower())


def sortStudentListByStudentID(studentList: list[Student]) -> list[Student]:
    """
    Sort the student list by student ID numerically.
    
    action: Sorts a list of Student objects by their idNumber attribute.
    input: studentList (list[Student]): List of Student objects to sort.
    output: None
    return: list[Student] - Sorted list of Student objects.
    """
    return sorted(studentList, key=lambda student: student.idNumber)


def displayFullAcademicReportSortedByLastName(studentList: list[Student]) -> None:
    """
    Display the Full Academic Report sorted by last name (menu option 9).
    
    action: Sorts students by last name and displays the full academic report.
    input: studentList (list[Student]): List of Student objects.
    output: None
    return: None
    """
    sortedList = sortStudentListByLastName(studentList)
    displayFullStudentAcademicReport(sortedList)


def displayFullAcademicReportSortedByStudentID(studentList: list[Student]) -> None:
    """
    Display the Full Academic Report sorted by student ID (menu option 10).
    
    action: Sorts students by student ID and displays the full academic report.
    input: studentList (list[Student]): List of Student objects.
    output: None
    return: None
    """
    sortedList = sortStudentListByStudentID(studentList)
    displayFullStudentAcademicReport(sortedList)


# Menu & Main Menu function
def createMenu(employeeList: list[Employee], studentList: list[Student]) -> None:
    """
    Create and display the main menu, handling user input.
    
    action: Displays a menu and processes user selections.
    input: employeeList (list[Employee]): List of Employee objects.
           studentList (list[Student]): List of Student objects.
    output: None
    return: None
    """
    while True:
        print("\nPlease select an option below\n")
        print("1. Quit")
        print("2. Display Student Contact Information")
        print("3. Display Employee Contact Information")
        print("4. Display All Persons Contact Information")
        print("5. Display Employee Employment Information")
        print("6. Display Full Academic Report")
        print("7. Display Academic Report for one Student")
        print("8. Display Honor Roll")
        print("9. Display Full Academic Report sorted by Last Name")
        print("10. Display Full Academic Report sorted by Student ID")
        choice = input("\n> ").strip()
        
        # Handle menu choice with match-cases instead of if-elif-else 
        match choice:
            case '1':
                print("\nThank you for using the system.")
                print("Now exiting the program…")
                break
            case '2':
                displayStudentContactInformation(studentList)
            case '3':
                displayEmployeeContactInformation(employeeList)
            case '4':
                displayAllPersonContactInformation(employeeList, studentList)
            case '5':
                displayEmployeeEmploymentInformation(employeeList)
            case '6':
                displayFullStudentAcademicReport(studentList)
            case '7':
                lookUpStudentAcademicRecord(studentList)
            case '8':
                getHonorRoll(studentList)
            case '9':
                displayFullAcademicReportSortedByLastName(studentList)
            case '10':
                displayFullAcademicReportSortedByStudentID(studentList)
            case _:
                print("Invalid choice. Please select 1-10.")

# Main function
def main() -> None:
    """
    Main function to start the application.
    
    action: Initializes the application, loads data, and starts the menu.
    input: None
    output: None
    return: None
    """
    print("Starting application…")
    employees = getEmployees('employees.txt')
    students = getStudents('students.txt')
    # Load scores for students
    getStudentScores(students, 'scores.txt')
    print("\nWelcome to the College Data System")
    createMenu(employees, students)

# Run main function
if __name__ == "__main__":
    main()
