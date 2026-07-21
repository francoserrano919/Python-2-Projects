"""
script: Serrano_Software_Engineering_Abstract_Classes.py

Action:
    a. Defines an abstract employee class with required earnings() method
    b. Implements salaried_employee and hourly_employee subclasses
    c. Validates input for all fields (names, ssn, salary, hours, wage)
    d. Demonstrates instantiation, __repr__, __str__, and polymorphic payroll
    e. Shows error handling for abstract class instantiation and invalid input

Author: Franco Xavier Serrano
Date: 10/15/2025
"""

# Imports
from __future__ import annotations
from abc import ABC, abstractmethod
import re

# Constants for payroll calculations
REGULAR_HOURS = 40.0
OVERTIME_MULTIPLIER = 1.5
MAX_WEEKLY_HOURS = 168.0


class Employee(ABC):
    """
    Abstract base class: a generic employee with core identity fields.
    """

    def __init__(self, first_name: str, last_name: str, ssn: str):
        '''
        Read-only via properties (no setters provided)
        action: store and validate first name, last name, ssn
        input: first_name (str), last_name (str), ssn (str)
        output: stored values or ValueError on invalid input
        return: none
        '''
        self._first_name = str(first_name).strip() # _ to indicate "protected"
        self._last_name = str(last_name).strip() # _ to indicate "protected"
        self._ssn = str(ssn).strip() # _ to indicate "protected"

        # Validation for first name, last name, and SSN
        if not self._first_name or not self._last_name:
            raise ValueError("first_name and last_name must be non-empty strings.")

        # Stricter SSN format check: XXX-XX-XXXX
        if not re.match(r'^\d{3}-\d{2}-\d{4}$', self._ssn):
            raise ValueError("ssn must be in format XXX-XX-XXXX (e.g., 123-45-6789).")

    # Show read-only properties for first_name, last_name, ssn
    @property
    def first_name(self) -> str:
        return self._first_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @property
    def ssn(self) -> str:
        return self._ssn

    # Abstract method for earnings calculation
    @abstractmethod
    def earnings(self) -> float:
        """Return weekly pay for this employee."""
        raise NotImplementedError("Subclasses must implement earnings().")

    # __repr__ method for string representation
    def __repr__(self) -> str:
        # Assignment asks for a string containing first name, last name, and SSN.
        # Kept it simple so subclasses can prefix it cleanly.
        return f"{self.first_name} {self.last_name}; SSN: {self.ssn}"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} (SSN: {self.ssn})"

# SalariedEmployee subclass of Employee
class SalariedEmployee(Employee):
    """
    Employee paid a fixed weekly salary.
    """

    def __init__(self, first_name: str, last_name: str, ssn: str, weekly_salary: float):
        super().__init__(first_name, last_name, ssn)
        self.weekly_salary = weekly_salary  # validates via setter

    @property
    def weekly_salary(self) -> float:
        return self._weekly_salary

    @weekly_salary.setter
    def weekly_salary(self, value: float) -> None:
        try:
            value = float(value)
        except (TypeError, ValueError):
            raise ValueError("weekly_salary must be a number.") from None
        if value < 0:
            raise ValueError("weekly_salary must be non-negative.")
        self._weekly_salary = value

    def earnings(self) -> float:
        return self.weekly_salary

    # --- Spec-required repr that prefixes and calls base version ---
    def __repr__(self) -> str:
        return f"SalariedEmployee: {super().__repr__()}, weekly_salary: {self.weekly_salary:.2f}"

# HourlyEmployee subclass of Employee
class HourlyEmployee(Employee):
    """
    Employee paid by the hour, with 1.5x overtime beyond 40 hours.

    Note: For real-world payroll, use decimal.Decimal for currency to avoid float rounding errors.
    """

    def __init__(self, first_name: str, last_name: str, ssn: str, hours: float, wage: float):
        super().__init__(first_name, last_name, ssn)
        self.hours = hours   # validates via setter
        self.wage = wage

    @property
    def hours(self) -> float:
        return self._hours

    @hours.setter
    def hours(self, value: float) -> None:
        try:
            value = float(value)
        except (TypeError, ValueError):
            raise ValueError("hours must be a number.") from None
        if not (0.0 <= value <= MAX_WEEKLY_HOURS):
            raise ValueError(f"hours must be in the range [0, {MAX_WEEKLY_HOURS}].")
        self._hours = value

    @property
    def wage(self) -> float:
        return self._wage

    @wage.setter
    def wage(self, value: float) -> None:
        try:
            value = float(value)
        except (TypeError, ValueError):
            raise ValueError("wage must be a number.") from None
        if value < 0.0:
            raise ValueError("wage must be non-negative.")
        self._wage = value

    def earnings(self) -> float:
        base = min(self.hours, REGULAR_HOURS) * self.wage
        overtime = max(self.hours - REGULAR_HOURS, 0.0) * OVERTIME_MULTIPLIER * self.wage
        return base + overtime

    # Assignment asked for a repr that prefixes and calls base version
    def __repr__(self) -> str:
        return (
            f"HourlyEmployee: {super().__repr__()}, "
            f"hours: {self.hours:.2f}, wage: {self.wage:.2f}"
        )

# Function self-named demo() to demonstrate functionality of the above classes
def demo() -> None:
    """
    Demonstrates abstract class behavior and polymorphic earnings().
    action: Shows a demonstration of abstract classes and polymorphism
    input: none
    output: Demonstrates abstract class behavior and polymorphic earnings.
    return: none
    """
    

    # Shows that abstract classes cannot be instantiated directly
    print("— Abstract class instantiation check —")
    try:
        _ = Employee("Ada", "Lovelace", "000-00-0000")  # type: ignore[abstract]
    except TypeError as e:
        print("As expected, Employee() fails:", e)
    print()

    # Creates concrete employees. Names are taken from famous computer scientists
    # like in the examples from the CIS 129 book.
    salaried_employee = SalariedEmployee("Grace", "Hopper", "111-11-1111", weekly_salary=1500)
    hourly_employee = HourlyEmployee("Alan", "Turing", "222-22-2222", hours=46, wage=40)

    # Print out the employees (objects) using both repr and str, and show their earnings
    print("— Concrete employees —")
    for employee in (salaried_employee, hourly_employee):
        print(repr(employee))
        print(str(employee))
        print(f"Earnings: ${employee.earnings():,.2f}")
        print()

    # Polymorphic processing
    print("— Polymorphic payroll loop —")
    staff: list[Employee] = [salaried_employee, hourly_employee]
    total = 0.0
    for employee in staff:
        pay = employee.earnings()  # same call, different behavior per subclass
        print(f"{employee.first_name} {employee.last_name}: ${pay:,.2f}")
        total += pay
    print(f"Total payroll this week: ${total:,.2f}")

# Allows the script to be run directly.
if __name__ == "__main__":
    demo()
