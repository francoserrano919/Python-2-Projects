'''
script: project1Employees.py
action:
    a. Defines an Abstract Person Class with core identity and contact fields
    b. Implements Concrete Employee Subclass with employment-specific fields
    c. Validates input for all fields (names, id, email, phone, hire date, role, classification, salary)
    d. Loads employee data from a text file and creates Employee objects
    e. Provides interactive menu to display employee information
Author: Franco Xavier Serrano
Date: 10/28/2025
'''

from abc import ABC, abstractmethod
from datetime import date
import re
from typing import List


# Abstract base class Person
class Person(ABC):
    """
    Abstract person with core identity and contact info.

    action: Store and validate personal and contact information
    input: firstName (str), lastName (str), idNumber (int), emailAddress (str), phoneNumber (str)
    output: Stored values or ValueError on invalid input
    return: None
    """

    # Keep class abstract with at least one abstract member
    @abstractmethod
    def kind(self) -> str:
        """Return entity kind (e.g., 'Employee')."""
        raise NotImplementedError

    def __init__(self, firstName: str, lastName: str, idNumber: int,
                 emailAddress: str, phoneNumber: str) -> None:
        '''
        Initialize a Person with validated personal and contact information.

        action: Store and validate personal and contact information
        input: firstName (str), lastName (str), idNumber (int), emailAddress (str), phoneNumber (str)
        output: Stored values or ValueError on invalid input
        return: None
        '''
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
        if idNumber < 1000 or idNumber > 9999:
            raise ValueError("ID Number must be a 4-digit integer (1000-9999).")

        # Validate phone (###-###-####) and email minimally
        phoneNumber = str(phoneNumber).strip()
        if not re.fullmatch(r"\d{3}-\d{3}-\d{4}", phoneNumber):
            raise ValueError("Phone Number must be in the format ###-###-####.")
        emailAddress = str(emailAddress).strip()
        # Allow empty email; if provided, require '@'
        if emailAddress and "@" not in emailAddress:
            raise ValueError("Email Address must contain '@' when provided.")

        # Store (use leading underscore to indicate private)
        self._firstName = firstName
        self._lastName = lastName
        self._idNumber = idNumber
        self._emailAddress = emailAddress
        self._phoneNumber = phoneNumber

    # First Name property
    @property
    def firstName(self) -> str:
        return self._firstName

    # First Name setter
    @firstName.setter
    def firstName(self, value: str) -> None:
        value = str(value).strip()
        if not value:
            raise ValueError("First Name cannot be empty.")
        self._firstName = value

    # Last Name property
    @property
    def lastName(self) -> str:
        return self._lastName

    # Last Name setter
    @lastName.setter
    def lastName(self, value: str) -> None:
        value = str(value).strip()
        if not value:
            raise ValueError("Last Name cannot be empty.")
        self._lastName = value

    # Read-only idNumber
    @property
    def idNumber(self) -> int:
        return self._idNumber

    # Email Address property
    @property
    def emailAddress(self) -> str:
        return self._emailAddress

    # Email Address setter
    @emailAddress.setter
    def emailAddress(self, value: str) -> None:
        value = str(value).strip()
        # Allow empty email; if provided, require '@'
        if value and "@" not in value:
            raise ValueError("Email Address must contain '@' when provided.")
        self._emailAddress = value

    # Phone Number property
    @property
    def phoneNumber(self) -> str:
        return self._phoneNumber

    # Phone Number setter
    @phoneNumber.setter
    def phoneNumber(self, value: str) -> None:
        value = str(value).strip()
        if not re.fullmatch(r"\d{3}-\d{3}-\d{4}", value):
            raise ValueError("Phone Number must be in the format ###-###-####.")
        self._phoneNumber = value

    # Representation
    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(firstName={self.firstName!r}, "
                f"lastName={self.lastName!r}, idNumber={self.idNumber!r})")

    # String representation
    def __str__(self) -> str:
        return f"{self.lastName}, {self.firstName} ({self.idNumber})"


# Concrete Employee class
class Employee(Person):
    '''
    Concrete Employee class extending Person with additional employment details.

    action: Store and validate employment-specific information
    input: hireYear (int), hireMonth (int), hireDay (int),
           rolePerson (str), classificationPerson (str), annualSalary (float)
    output: Stored values or ValueError on invalid input
    return: None
    '''
    # Class variables (keys are strings with leading zeros)
    roleDictionary = {"001": "Staff", "002": "Faculty"}
    classificationDictionary = {"001": "Full", "002": "Part"}

    # Implement abstract member
    def kind(self) -> str:  # implements abstract member
        return "Employee"

    # Function initializer
    def __init__(self, firstName: str, lastName: str, idNumber: int,
                 emailAddress: str, phoneNumber: str,
                 hireYear: int, hireMonth: int, hireDay: int,
                 rolePerson: str, classificationPerson: str,
                 annualSalary: float) -> None:
        '''
        Initialize an Employee with validated employment details.

        action: Store and validate employment-specific information
        input: HireYear (int), hireMonth (int), hireDay (int),
               rolePerson (str key), classificationPerson (str key), annualSalary (float)
        output: Stored values or ValueError on invalid input
        return: None
        '''

        # Initialize base Person fields
        super().__init__(firstName, lastName, idNumber, emailAddress, phoneNumber)

        # Create the hire date INSIDE the class as required by the spec
        try:
            self._hireDate = date(int(hireYear), int(hireMonth), int(hireDay))
        except Exception as e:
            raise ValueError(f"Hire Date must be a valid date (MM/DD/YYYY parts): {e}")

        # Validate role and classification keys
        if rolePerson not in Employee.roleDictionary:
            raise ValueError("Role Person must be a key in roleDictionary (e.g., '001').")
        if classificationPerson not in Employee.classificationDictionary:
            raise ValueError("Classification Person must be a key in classificationDictionary (e.g., '001').")
        self._rolePerson = rolePerson
        self._classificationPerson = classificationPerson

        # Validate annual salary
        try:
            annualSalary = float(annualSalary)
        except (TypeError, ValueError):
            raise ValueError("Annual Salary must be a number.") from None
        if annualSalary < 0:
            raise ValueError("Annual Salary must be non-negative.")
        self._annualSalary = round(annualSalary, 2)

    # Read-only hireDate
    @property
    def hireDate(self) -> date:
        return self._hireDate

    # Role key
    @property
    def rolePerson(self) -> str:
        return self._rolePerson

    # Role key setter
    @rolePerson.setter
    def rolePerson(self, key: str) -> None:
        if key not in Employee.roleDictionary:
            raise ValueError("Role Person must be a valid key in roleDictionary.")
        self._rolePerson = key

    # Classification key
    @property
    def classificationPerson(self) -> str:
        return self._classificationPerson

    # Classification key setter
    @classificationPerson.setter
    def classificationPerson(self, key: str) -> None:
        if key not in Employee.classificationDictionary:
            raise ValueError("Classification Person must be a valid key in classificationDictionary.")
        self._classificationPerson = key

    # Annual Salary
    @property
    def annualSalary(self) -> float:
        return self._annualSalary

    # Annual Salary setter
    @annualSalary.setter
    def annualSalary(self, value: float) -> None:
        try:
            value = float(value)
        except (TypeError, ValueError):
            raise ValueError("Annual Salary must be a number.") from None
        if value < 0:
            raise ValueError("Annual Salary must be non-negative.")
        self._annualSalary = round(value, 2)

    # Representation
    def __repr__(self) -> str:
        return (f"Employee({self.lastName}, {self.firstName}, id={self.idNumber}, "
                f"role={self._rolePerson}, class={self._classificationPerson}, salary={self._annualSalary:.2f})")

    # String representation
    def __str__(self) -> str:
        return f"{self.lastName}, {self.firstName} | {self.idNumber} | {self.emailAddress} | {self.phoneNumber}"

# Function to map label to key
def label_to_key(mapping: dict, label: str) -> str | None:
    '''
    Map a label to its corresponding key.

    action: Map label to key using provided dictionary
    input: Mapping dictionary, label string
    output: Corresponding key or None if not found
    return: Key string or None
    '''
    # Case-insensitive lookup by value -> key
    label = str(label).strip().lower()

    # Accept common synonyms 
    synonyms = {
        "full-time": "001", "full time": "001", "full": "001",
        "part-time": "002", "part time": "002", "part": "002",
        "staff": "001" if "staff" in mapping.values() else None,
        "faculty": "002" if "faculty" in mapping.values() else None
    }
    if label in synonyms and synonyms[label] in mapping:
        return synonyms[label]

    for k, v in mapping.items():
        if str(v).strip().lower() == label:
            return k
    return None


# Data loading function
def getEmployees(file_path: str = 'employees.txt') -> List[Employee]:
    '''
    Load employee data from a text file.

    action: Read employee data from file and create Employee objects
    input: File path (default 'employees.txt')
    output: List of Employee objects
    return: List of Employee objects
    '''
    employeeList: List[Employee] = []
    print("\nAdding employees…\n")

    # Try to open the file and handle missing file gracefully
    try:
        f = open(file_path, 'r', encoding='utf-8')
    except FileNotFoundError:
        print(f"Error: '{file_path}' was not found. Place the file next to this script and try again.")
        return employeeList

    with f:
        header_skipped = False  # flag to skip header line

        # For loop to read each line
        for line in f:
            line = line.strip()
            if not line:
                continue
            # Skip header
            if not header_skipped:
                if line.lower().startswith('lastname'):
                    header_skipped = True
                    continue
                else:
                    header_skipped = True

            # Split on any whitespace (handles tabs and spaces)
            fields = re.split(r'\s+', line)
            if len(fields) < 9:
                print(f"Skipping row (malformed, expected 9 fields): {line}")
                continue
            last, first, id_str, email, phone, hire_str, classification_lbl, role_lbl, salary_str = fields[:9]

            # Map labels to keys
            role_key = label_to_key(Employee.roleDictionary, role_lbl)
            class_key = label_to_key(Employee.classificationDictionary, classification_lbl)
            if role_key is None or class_key is None:
                print(f"Skipping row (invalid role/classification): {first} {last}")
                continue

            # Parse hire date parts
            try:
                m, d, y = map(int, hire_str.split('/'))
            except Exception:
                print(f"Skipping row (invalid hire date '{hire_str}'): {line}")
                continue

            # Create Employee object with error handling
            try:
                emp = Employee(
                    firstName=first,
                    lastName=last,
                    idNumber=int(id_str),
                    emailAddress=email,
                    phoneNumber=phone,
                    hireYear=y,
                    hireMonth=m,
                    hireDay=d,
                    rolePerson=role_key,
                    classificationPerson=class_key,
                    annualSalary=float(salary_str)
                )
            except Exception as ex:
                print(f"Skipping row (error parsing record: {ex}): {line}")
                continue
            employeeList.append(emp)
            print(f"Added employee {emp.firstName} {emp.lastName}…")
    return employeeList


# Reporting function
def displayEmployeeEmploymentInformation(employeeList: List[Employee]) -> None:
    '''
    Display employee employment information.

    action: Output to user employee employment information
    input: Employee list
    output: Employee employment information
    return: None
    '''
    print("\n\t\t\tEmployee Employment Information\n")

    # Headers (no tabs; used spacing per project directions)
    print(f"{ 'LastName':<12}{ 'FirstName':<12}{ 'ID':<6}{ 'Email':<30}{ 'Phone':<14}{ 'HireDate':<12}{ 'Classification':<15}{ 'Role':<10}{ 'Salary':>12}")

    # For loop to index through employee list and print employment info
    for e in employeeList:
        hire_str = f"{e.hireDate.month}/{e.hireDate.day}/{e.hireDate.year}"
        classification = Employee.classificationDictionary.get(e.classificationPerson, '?')
        role = Employee.roleDictionary.get(e.rolePerson, '?')
        print(f"{e.lastName:<12}{e.firstName:<12}{e.idNumber:<6}{e.emailAddress:<30}{e.phoneNumber:<14}{hire_str:<12}{classification:<15}{role:<10}{e.annualSalary:>12.2f}")


# Function to display employee contact information
def displayEmployeeContactInformation(employeeList: List[Employee]) -> None:
    '''
    Display employee contact information.

    action: Output to user employee contact information
    input: Employee list
    output: Employee contact information
    return: None
    '''
    print("\n\t\tEmployee Contact Information\n")
    print(f"{ 'LastName':<12}{ 'FirstName':<12}{ 'ID':<6}{ 'Email':<30}{ 'Phone':<14}")

    # For loop to index through employee list and print contact info
    for e in employeeList:
        print(f"{e.lastName:<12}{e.firstName:<12}{e.idNumber:<6}{e.emailAddress:<30}{e.phoneNumber:<14}")


# Menu
def createMenu(employeeList: List[Employee]) -> None:
    '''
    Create and display the menu for employee information.
    
    action: Output to user interactive menu
    input: Employee list
    output: Interactive menu
    return: None
    '''
    while True:
        print("\nPlease select an option below\n")
        print("1. Quit")
        print("2. Display Employee Employment Information")
        print("3. Display Employee Contact Information")
        choice = input("\n>: ").strip()
        if choice == '1':
            print("\nThank you for using the system.\n\nNow exiting the program…")
            break
        elif choice == '2':
            displayEmployeeEmploymentInformation(employeeList)
        elif choice == '3':
            displayEmployeeContactInformation(employeeList)
        else:
            print(f"\nI am sorry, {choice} is not an option.")


# Main function
def main() -> None:
    '''
    Main function to start the application.

    action: Load employees and start menu
    input: none
    output: Interactive menu
    return: None
    '''
    print("Starting application…")
    employees = getEmployees()
    createMenu(employees)


# Allows the script to be run standalone
if __name__ == "__main__":
    main()
