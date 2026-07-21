'''
script: project2.py
action:
    a. Defines an Abstract Person class with core identity and contact fields
    b. Implements Employee and Student subclasses
    c. Validates input for all fields (names, id, email, phone, hire date, role, classification, salary)
    d. Loads employee and student data from text files and creates objects
    e. Provides interactive menu to display employee, student and combined information
Author: Franco Xavier Serrano
Date: 11/13/2025
'''

from abc import ABC
from datetime import date
import re
from pathlib import Path


# Abstract Base Class: Person
class Person(ABC):
    """
    Class Person: Abstract base class for individuals with identity and contact information.

    action: Define core identity and contact fields with validation
    input: firstName, lastName, idNumber, emailAddress, phoneNumber
    output: Person object with validated fields
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

    # Setter with validation
    @firstName.setter
    def firstName(self, value: str) -> None:
        value = str(value).strip()
        if not value:
            raise ValueError("First Name must be non-empty.")
        self._firstName = value

    # Last Name property
    @property
    def lastName(self) -> str:
        return self._lastName

    # Setter with validation
    @lastName.setter
    def lastName(self, value: str) -> None:
        value = str(value).strip()
        if not value:
            raise ValueError("Last Name must be non-empty.")
        self._lastName = value

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
        """
        Function to set email address with validation.

        action: Validate email format when setting
        input: emailAddress (str)
        output: None
        """
        value = str(value).strip()
        
        # Validate email format
        if value and "@" not in value:
            raise ValueError("Email Address must contain '@' when provided.")
        self._emailAddress = value

    # Phone
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
    
    action: Define employment-specific fields with validation
    input: hireDate, rolePerson, classificationPerson, annualSalary
    output: Employee object with validated fields
    return: None
    """
    
    # Dictionaries for role and classification
    roleDictionary = {"001": "Staff", "002": "Faculty"}
    classificationDictionary = {"001": "Full", "002": "Part"}

    # Provide a concrete default that subclasses may override.
    def kind(self) -> str:
        return "Employee"

    # Function to initialize Employee object
    def __init__(self, firstName: str, lastName: str, idNumber: int,
                 emailAddress: str, phoneNumber: str,
                 hireYear: int, hireMonth: int, hireDay: int,
                 rolePerson: str, classificationPerson: str,
                 annualSalary: float) -> None:
        super().__init__(firstName, lastName, idNumber, emailAddress, phoneNumber)
        """
        Initialize an Employee object with validated fields.

        action: Validate and set hire date, role, classification, and salary
        input: hireYear, hireMonth, hireDay, rolePerson, classificationPerson, annual
        output: None
        return: None
        """

        # Hire date
        try:
            self._hireDate = date(int(hireYear), int(hireMonth), int(hireDay))
        except Exception as e:
            raise ValueError(f"Hire Date must be a valid date (MM/DD/YYYY parts): {e}")

        # Role and classification keys
        if rolePerson not in Employee.roleDictionary:
            raise ValueError("Role Person must be a key in roleDictionary (e.g., '001').")
        if classificationPerson not in Employee.classificationDictionary:
            raise ValueError("Classification Person must be a key in classificationDictionary (e.g., '001').")
        self._rolePerson = rolePerson
        self._classificationPerson = classificationPerson

        # Salary
        try:
            annualSalary = float(annualSalary)
        except (TypeError, ValueError):
            raise ValueError("Annual Salary must be a number.") from None
        if annualSalary < 0:
            raise ValueError("Annual Salary must be non-negative.")
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
            raise ValueError("Invalid role key.")
        self._rolePerson = key

    # Classification property
    @property
    def classificationPerson(self) -> str:
        return self._classificationPerson

    # Setter with validation
    @classificationPerson.setter
    def classificationPerson(self, key: str) -> None:
        if key not in Employee.classificationDictionary:
            raise ValueError("Invalid classification key.")
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
            raise ValueError("Annual Salary must be a number.") from None
        if value < 0:
            raise ValueError("Annual Salary must be non-negative.")
        self._annualSalary = round(value, 2)

    # String representation
    def __repr__(self) -> str:
        return (f"Employee({self.lastName}, {self.firstName}, id={self.idNumber}, "
                f"role={self._rolePerson}, class={self._classificationPerson}, salary={self._annualSalary:.2f})")

    # String representation
    def __str__(self) -> str:
        return f"{self.lastName}, {self.firstName} | {self.idNumber} | {self.emailAddress} | {self.phoneNumber}"


# Student Class
class Student(Person):
    """
    Class Student: Concrete subclass of Person with student-specific fields.

    action: Define student-specific fields with validation
    input: None (inherits from Person)
    output: Student object with validated fields
    return: None
    """

    # Provide a concrete default that subclasses may override.
    def __init__(self, firstName: str, lastName: str, idNumber: int,
                 emailAddress: str, phoneNumber: str) -> None:
        # Explicit __init__ to satisfy rubric, delegating to Person
        super().__init__(firstName, lastName, idNumber, emailAddress, phoneNumber)

    # Function to initialize Student object
    def kind(self) -> str:
        return "Student"

    # Function to represent Student object
    def __repr__(self) -> str:
        return f"Student({self.lastName}, {self.firstName}, id={self.idNumber})"

    # Function to represent Student object
    def __str__(self) -> str:
        # Explicit __str__ to satisfy rubric, using Person behavior
        return super().__str__()


# Helpers to map labels to keys
def label_to_key(mapping: dict, label: str) -> str | None:
    """
    Map a label (like 'Full', 'Staff') to its key ('001'/'002').

    action: Map label to corresponding key in mapping
    input: label (str)
    output: key (str | None)
    return: None
    """
    if not label:
        return None
    label_norm = str(label).strip().lower()

    # Direct value match
    for k, v in mapping.items():
        if str(v).strip().lower() == label_norm:
            return k

    # Common synonyms to keys
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


# Function to open data file with last resort in case of missing file
def _open_data_file(path: str | Path) -> Path:
    """
    Locate a data file.

    In case of misplaced files, this will help find them.
    """
    p = Path(path)
    if p.exists():
        return p
    fallback = Path.home() / 'Downloads' / p.name
    if fallback.exists():
        return fallback
    raise FileNotFoundError(f"Data file not found at {p} or {fallback}. Place the file next to the script or in ~/Downloads.")

# Function to split columns in data line
def _split_columns(line: str, expected: int) -> list[str] | None:
    """
    Split a data line by tabs, then 2+ spaces, then any spaces; trying to get the same columns as example output.
    
    action: Split line into columns based on delimiters
    input: line (str), expected number of columns (int)
    output: List of columns or None
    return: list[str] | None
    """
    line = line.strip()
    if not line:
        return None

    # For loop to try different splitting patterns
    for pattern in (r"\t+", r"\s{2,}", r"\s+"):
        parts = re.split(pattern, line)
        if len(parts) >= expected:
            return parts
    return None


# Function to load employees from file
def getEmployees(file_path: str = 'employees.txt') -> list[Employee]:
    """
    Load employees from a text file and return a list of Employee objects.

    action: Read employee data file and create Employee objects
    input: File path to employee data
    output: List of Employee objects
    return: list[Employee]
    """
    employeeList: list[Employee] = []
    print("\nAdding employees…\n")
    try:
        p = _open_data_file(file_path)
    except FileNotFoundError:
        print(f"Error: '{file_path}' was not found in CWD or ~/Downloads.")
        return employeeList

    # Read file and create Employee objects
    with p.open('r', encoding='utf-8') as f:
        header_skipped = False
        for line in f:
            if not header_skipped:
                header_skipped = True
                continue
            parts = _split_columns(line, expected=9)
            if not parts:
                continue
            last, first, id_str, email, phone, hire_str, class_lbl, role_lbl, salary_str = parts[:9]
            
            # Parse date m/d/yyyy
            try:
                m, d, y = [int(x) for x in hire_str.split('/')]
            except Exception:
                continue
            class_key = label_to_key(Employee.classificationDictionary, class_lbl) or class_lbl
            role_key = label_to_key(Employee.roleDictionary, role_lbl) or role_lbl

            # Try block to create Employee object
            try:
                emp = Employee(first, last, int(id_str), email, phone, y, m, d, role_key, class_key, float(salary_str))
                employeeList.append(emp)
                print(f"Added employee {first} {last}…")
            except Exception as e:
                print(f"Skipping employee '{first} {last}' due to error: {e}")
                continue
    return employeeList


# Function to load students from file
def getStudents(file_path: str = 'students.txt') -> list[Student]:
    """
    Load students from a text file and return a list of Student objects.

    action: Read student data file and create Student objects
    input: File path to student data
    output: List of Student objects
    return: list[Student]
    """
    studentList: list[Student] = []
    print("\nAdding students…\n")
    try:
        p = _open_data_file(file_path)
    except FileNotFoundError:
        print(f"Error: '{file_path}' was not found in CWD or ~/Downloads.")
        return studentList

    # Read file and create Student objects
    with p.open('r', encoding='utf-8') as f:
        header_skipped = False

        # For loop to read each line
        for line in f:
            if not header_skipped:
                header_skipped = True
                continue
            parts = _split_columns(line, expected=5)
            if not parts:
                continue
            last, first, id_str, email, phone = parts[:5]

            # Try block to create Student object
            try:
                student = Student(first, last, int(id_str), email, phone)
                studentList.append(student)
                print(f"Added student {first} {last}…")
            except Exception as e:
                print(f"Skipping student '{first} {last}' due to error: {e}")
                continue
    return studentList


# Functions to display reports
def displayEmployeeEmploymentInformation(employeeList: list[Employee]) -> None:
    """
    Display employment information for each employee.

    action: Print formatted employment info table
    input: List of Employee objects
    output: Formatted table to console
    return: None
    """

    print("\n\t\t\tEmployee Employment Information\n")
    print(f"{'LastName':<12}{'FirstName':<12}{'ID':<6}{'Email':<30}{'Phone':<14}{'HireDate':<12}{'Classification':<15}{'Role':<10}{'Salary':>12}")
    
    # Iterate and print each employee's info
    for e in employeeList:
        hire_str = f"{e.hireDate.month}/{e.hireDate.day}/{e.hireDate.year}"
        classification = Employee.classificationDictionary.get(e.classificationPerson, '?')
        role = Employee.roleDictionary.get(e.rolePerson, '?')
        print(f"{e.lastName:<12}{e.firstName:<12}{e.idNumber:<6}{e.emailAddress:<30}{e.phoneNumber:<14}{hire_str:<12}{classification:<15}{role:<10}{e.annualSalary:>12.2f}")

# Function to display employee contact information
def displayEmployeeContactInformation(employeeList: list[Employee]) -> None:
    """
    Display contact information for each employee.

    action: Print formatted contact info table
    input: List of Employee objects
    output: Formatted table to console
    return: None
    """
    print("\n\t\tEmployee Contact Information\n")
    print(f"{'LastName':<12}{'FirstName':<12}{'ID':<6}{'Email':<30}{'Phone':<14}")
    for e in employeeList:
        print(f"{e.lastName:<12}{e.firstName:<12}{e.idNumber:<6}{e.emailAddress:<30}{e.phoneNumber:<14}")

# Function to display student contact information
def displayStudentContactInformation(studentList: list[Student]) -> None:
    """
    Display contact information for each student.

    action: Print formatted contact info table
    input: List of Student objects
    output: Formatted table to console
    return: None
    """
    print("\n\t\tStudent Contact Information\n")
    print(f"{'LastName':<12}{'FirstName':<12}{'ID':<6}{'Email':<30}{'Phone':<14}")
    for s in studentList:
        print(f"{s.lastName:<12}{s.firstName:<12}{s.idNumber:<6}{s.emailAddress:<30}{s.phoneNumber:<14}")

# Function to display all person contact information
def displayAllPersonContactInformation(employeeList: list[Employee], studentList: list[Student]) -> None:
    """
    Display contact information for all persons (employees and students).

    action: Print formatted contact info table
    input: Lists of Employee and Student objects
    output: Formatted table to console
    return: None
    """
    print("\n\t\tAll Person Contact Information\n")
    print(f"{'LastName':<12}{'FirstName':<12}{'ID':<6}{'Email':<30}{'Phone':<14}")
    personList: list[Person] = []
    personList.extend(employeeList)
    personList.extend(studentList)
    for p in personList:
        print(f"{p.lastName:<12}{p.firstName:<12}{p.idNumber:<6}{p.emailAddress:<30}{p.phoneNumber:<14}")


# Menu & Main
def createMenu(employeeList: list[Employee], studentList: list[Student]) -> None:
    """
    Create and display the menu for the application.

    action: Display menu and handle user choices
    input: User menu choice
    output: Displays requested information or exits
    return: None
    """
    while True:
        print("\nPlease select an option below\n")
        print("1. Quit")
        print("2. Display Employee Employment Information")
        print("3. Display Employee Contact Information")
        print("4. Display Student Contact Information")
        print("5. Display All Person Contact Information")
        choice = input("\n> ").strip()
        if choice == '1':
            print("\nThank you for using the system.\n\nNow exiting the program…")
            break
        elif choice == '2':
            displayEmployeeEmploymentInformation(employeeList)
        elif choice == '3':
            displayEmployeeContactInformation(employeeList)
        elif choice == '4':
            displayStudentContactInformation(studentList)
        elif choice == '5':
            displayAllPersonContactInformation(employeeList, studentList)
        else:
            print(f"\nI am sorry, {choice} is not an option.")


# Main function
def main() -> None:
    """
    Main function to start the application.

    action: Load data and start menu
    input: None
    output: None
    return: None
    """
    print("Starting application…")
    employees = getEmployees()
    students = getStudents()
    print("\nWelcome to the College Data System")
    createMenu(employees, students)


# Run the main function
if __name__ == "__main__":
    main()
