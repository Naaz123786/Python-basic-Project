import random

class BankAccount:
    def __init__(self, name, acc_no):
        self.name = name
        self.acc_no = acc_no
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful.")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print("Available balance:", self.balance)

# Dictionary to store account details
accounts = {}

def create_account():
    name = input("Enter your name: ")
    # Generate a random 6-digit account number
    acc_no = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    account = BankAccount(name, acc_no)
    accounts[acc_no] = account  # Store account in the dictionary
    return account

def access_account():
    name = input("Enter your name: ")
    acc_no = input("Enter your account number: ")
    # Check if the provided account number exists in the dictionary
    if acc_no in accounts and accounts[acc_no].name == name:
        print("Authentication successful")
        return accounts[acc_no]
    else:
        print("Authentication failed. Invalid name or account number.")
        return None

def main():
    while True:
        print("\nPROJECT")
        print("1. Create a new account")
        print("2. Access an existing account")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            account = create_account()
            print("Account created successfully.")
            print(f"Welcome, {account.name}! Your account number is {account.acc_no}.")
        elif choice == '2':
            account = access_account()
            if account:
                while True:
                    print("\n1. Withdrawal")
                    print("2. Deposit")
                    print("3. Display available balance")
                    print("4. Go back to previous menu")

                    option = input("Enter your option: ")

                    if option == '1':
                        amount = float(input("Enter withdrawal amount: "))
                        account.withdraw(amount)
                    elif option == '2':
                        amount = float(input("Enter amount to be deposited: "))
                        account.deposit(amount)
                    elif option == '3':
                        account.display_balance()
                    elif option == '4':
                        break
                    else:
                        print("Invalid option.")
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()