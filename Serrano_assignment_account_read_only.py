# make the account provide read-only properties for the name and balance.
# Rename class attributes with single leading underscores.
# test within ipython session to test updated class to confirm name and balance are read only

# account.py
"""Account class definition."""
from decimal import Decimal

class Account:
    """Account class for maintaining a bank account balance."""
    
    def __init__(self, name: str, balance: Decimal):
        """Initialize an Account object."""

        # if balance is less than 0.00, raise an exception
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00.')
        
        # Renamed attributes to _name and _balance
        self._name = name
        self._balance = balance
        
    @property
    # New getter method to provide read-only access to name
    def name(self) -> str:
        """Read-only property for account name."""
        # Renamed attribute to _name
        return self._name
    
    # Added setter to prevent modification of name
    @name.setter
    def name(self, _):
        raise AttributeError("Account name is read-only")

    @property
    # New getter method to provide read-only access to balance
    def balance(self) -> Decimal:
        """Read-only property for account balance."""
        # Renamed attribute to _balance
        return self._balance

    # Added setter to prevent modification of balance
    @balance.setter
    def balance(self, _): # Added _ to indicate variable is seen, but will not be used
        raise AttributeError("Account balance is read-only")
    

    def deposit(self, amount: Decimal):
        """Deposit money to the account."""
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')
        # Renamed attribute to _balance
        self._balance += amount

    def withdraw(self, amount: Decimal):
        """Withdraw money from the account."""
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')
        # Renamed attribute to _balance
        if amount > self._balance:
            raise ValueError('Insufficient funds.')
        # Renamed attribute to _balance
        self._balance -= amount

    def get_balance(self) -> Decimal:
        """Return the current balance."""
        # Renamed attribute to _balance
        return self._balance

    def __str__(self) -> str:
        return f"Account({self.name}, Balance: ${self.balance:.2f})"

if __name__ == "__main__":
    acct = Account("John Doe", Decimal("100.00"))
    print(acct)
    acct.deposit(Decimal("50.00"))
    print(f"\tAfter deposit: {acct}")
    acct.withdraw(Decimal("30.00"))
    print(f"\tAfter withdrawal: {acct}")
    print(f"\tCurrent balance: ${acct.get_balance():.2f}")




