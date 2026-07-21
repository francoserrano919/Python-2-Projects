# timewithproperties.py
"""Class Time with read-write properties using total seconds since midnight.

Demonstrates the use of property decorators to manage read-write access 
to hour, minute, and second attributes that are all derived from one 
internal variable: total seconds since midnight.

Action:
    a. Stores time as total seconds instead of three separate integers.
    b. Converts between total seconds and hours/minutes/seconds automatically.
    c. Demonstrates validation and mutation of attributes.
    d. Prints various object representations and shows error handling.
Author: Franco Xavier Serrano
Date: 10/15/2025
"""

class Time:
    """Class Time with read-write properties."""

    def __init__(self, hour=0, minute=0, second=0):
        """
        Initialize time as total seconds since midnight.
        action: store and validate hour, minute, second
        input: hour (int), minute (int), second (int)
        output: stored values or ValueError on invalid input    
        return: none
        """
        if not (0 <= hour < 24):
            raise ValueError(f'Hour ({hour}) must be 0-23')
        if not (0 <= minute < 60):
            raise ValueError(f'Minute ({minute}) must be 0-59')
        if not (0 <= second < 60):
            raise ValueError(f'Second ({second}) must be 0-59')

        # Store time as total seconds since midnight
        self._total_seconds = hour * 3600 + minute * 60 + second

    @property
    def hour(self):
        # Return the hour (0-23).
        return self._total_seconds // 3600  # Convert total seconds to hours

    @hour.setter
    def hour(self, hour):
        # Set the hour (0-23) while keeping minute and second unchanged.
        if not (0 <= hour < 24):
            raise ValueError(f'Hour ({hour}) must be 0-23')

        # Recalculate total seconds keeping minutes and seconds
        self._total_seconds = hour * 3600 + self.minute * 60 + self.second

    @property
    def minute(self):
        # Return the minute (0-59).
        return (self._total_seconds % 3600) // 60  # Convert remaining seconds to minutes

    @minute.setter
    def minute(self, minute):
        # Set the minute (0-59) while keeping hour and second unchanged.
        if not (0 <= minute < 60):
            raise ValueError(f'Minute ({minute}) must be 0-59')

        # Recalculate total seconds keeping hours and seconds
        self._total_seconds = self.hour * 3600 + minute * 60 + self.second

    @property
    def second(self):
        """Return the second (0-59)."""
        return self._total_seconds % 60  # Remaining seconds after removing hours and minutes

    @second.setter
    def second(self, second):
        # Set the second (0-59) while keeping hour and minute unchanged.
        if not (0 <= second < 60):
            raise ValueError(f'Second ({second}) must be 0-59')

        # Recalculate total seconds keeping hours and minutes
        self._total_seconds = self.hour * 3600 + self.minute * 60 + second

    def set_time(self, hour=0, minute=0, second=0):
        # Set all time components with validation."""
        self.hour = hour
        self.minute = minute
        self.second = second

    def to_universal_str(self):
        # Return time in universal (24-hour) format as HH:MM:SS.
        return f'{self.hour:02}:{self.minute:02}:{self.second:02}'

    def __repr__(self):
        # Return string representation for debugging and recreation.
        return (f'Time(hour={self.hour}, minute={self.minute}, '
                f'second={self.second})')

    def __str__(self):
        # Return user-friendly 12-hour formatted time string.
        hour_12 = 12 if self.hour in (0, 12) else self.hour % 12
        period = 'AM' if self.hour < 12 else 'PM'
        return f'{hour_12}:{self.minute:02}:{self.second:02} {period}'


# -------------------------------------------------------------------------
# Demonstration Section shows outputs and error handling
# -------------------------------------------------------------------------
if __name__ == '__main__':
    """Demonstrates creation, modification, and validation of Time objects.
    action: output to user demonstrations of Time class capabilities
    input: none
    output: demonstration of Time class capabilities
    return: none
    """
    print('--- Demonstrating the Time class ---\n')

    # Create several Time objects
    time_default = Time()                 # Defaults to 00:00:00
    time_noon = Time(12, 0, 0)            # 12:00:00 PM
    time_evening = Time(18, 45, 30)       # 6:45:30 PM

    # Display initial objects
    print('Created Time objects:')
    print(' time_default:', time_default, '| universal:', time_default.to_universal_str())
    print(' time_noon   :', time_noon,    '| universal:', time_noon.to_universal_str())
    print(' time_evening:', time_evening, '| universal:', time_evening.to_universal_str())
    print()

    # Modify time values using property setters
    print('Modifying time_evening...')
    time_evening.hour = 20  # 8 PM
    time_evening.minute = 15
    time_evening.second = 45

    print('After modification:')
    print(' time_evening:', time_evening, '| universal:', time_evening.to_universal_str())
    print()

    # Demonstrate set_time method
    print('Using set_time to reset time_default to 23:59:59...')
    time_default.set_time(23, 59, 59)
    print(' time_default:', time_default, '| universal:', time_default.to_universal_str())
    print()

    # Show repr representation for debugging
    print('Repr representation examples:')
    print(repr(time_default))
    print(repr(time_noon))
    print(repr(time_evening))
    print()

    # Demonstrate validation (will trigger exceptions)
    print('Demonstrating validation errors:')
    try:
        time_error = Time(25, 0, 0)
    except ValueError as e:
        print('Caught error:', e)
    try:
        time_noon.minute = 70
    except ValueError as e:
        print('Caught error:', e)
    print()

    print('--- End of demonstration ---')
