# 6. Write a Python class BankAccount with attributes like account_number, balance,
# date_of_opening and customer_name, and methods like deposit, withdraw, and
# check_balance.

class BankAccount:
    def __init__(self, account_number, customer_name, balance, date_of_opening):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
        self.date_of_opening = date_of_opening

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:}\nNew balance is ${self.balance:}")


    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:}\nNew balance is ${self.balance:}.")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Account balance: ${self.balance:}")

    def __str__(self):
        return (f"Account Number: {self.account_number}\n"
                f"Customer Name: {self.customer_name}\n"
                f"Balance: ${self.balance: }\n"
                f"Date of Opening: {self.date_of_opening}")


# Example usage
def main():
    account = BankAccount("10101010101", "rayyyy", 2000, "11-09-2024")

    print(account)

    account.deposit(500)
    account.withdraw(150)
    account.check_balance()
    account.withdraw(500)


main()
