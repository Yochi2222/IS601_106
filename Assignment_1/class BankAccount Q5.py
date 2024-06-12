class BankAccount:
  """Represents a bank account with basic functionalities."""

  def __init__(self, account_number, account_holder, balance):
    self.account_number = account_number
    self.balance = balance
    self.account_holder = account_holder

  def deposit(self, amount):
    """Deposits the specified amount into the account balance."""
    self.balance += amount
    print(f"Deposited ${amount}. New balance: ${self.balance:.2f}")

  def withdraw(self, amount):
    """Withdraws the specified amount from the account balance,
    but prevents overdraft."""
    if amount > self.balance:
      print(f"Insufficient funds. Current balance: ${self.balance:.2f}")
    else:
      self.balance -= amount
      print(f"Withdrew ${amount}. New balance: ${self.balance:.2f}")

  def get_balance(self):
    """Returns the current balance of the account."""
    return self.balance


class CheckingAccount(BankAccount):
  """Represents a checking account with transaction fees."""

  def __init__(self, account_number, account_holder, balance, transaction_fees):
    super().__init__(account_number, account_holder, balance)
    self.transaction_fees = transaction_fees

  def apply_transaction_fees(self):
    """Subtracts the transaction fees from the current balance."""
    self.balance -= self.transaction_fees
    print(f"Applied transaction fee of ${self.transaction_fees:.2f}. New balance: ${self.balance:.2f}")


class SavingsAccount(BankAccount):
  """Represents a savings account with interest calculation."""

  def __init__(self, account_number, account_holder, balance, interest_rate):
    super().__init__(account_number, account_holder, balance)
    self.interest_rate = interest_rate

  def calculate_interest(self):
    """Calculates and adds the interest to the current balance."""
    interest = self.balance * self.interest_rate
    self.balance += interest
    print(f"Interest earned: ${interest:.2f}. New balance: ${self.balance:.2f}")


# Create a BankAccount instance
bank_account = BankAccount(123456, "John Doe", 1000.00)

# Call deposit and withdraw methods
bank_account.deposit(200.00)
bank_account.withdraw(700.00)

# Print the final balance
print(f"Total balance: ${bank_account.get_balance():.2f}")

# Create a CheckingAccount instance
checking_account = CheckingAccount(654321, "Jane Doe", 500.00, 34.50)

# Apply transaction fees
checking_account.apply_transaction_fees()

# Print the final balance
print(f"Total balance: ${checking_account.get_balance():.2f}")

# Create a SavingsAccount instance
savings_account = SavingsAccount(789012, "Alice Smith", 800.00, 0.12)

# Calculate interest
savings_account.calculate_interest()

# Print the final balance
print(f"Total balance: ${savings_account.get_balance():.2f}")