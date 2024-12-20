import bank_account
from bank_account import BankAccount

account = bank_account.BankAccount("7101968", "1234", "Danny de Vet", 500.00)

print(f"Saldo: € {account.balance:.2f}")

account.deposit(42.00)
print(f"You deposited €42 on your account, your new balance is: €{account.balance:.2f}")

account.withdraw(20.00)
print(f"You withdraw €20,00 from your account, your new balance is: €{account.balance:.2f}")

print("\n The three account id's for testing purposes")
print("      7101968  pin 1234   Danny de Vet      1000")
print("      1234567  pin 4567   Urbanus Van Anus  500")
print("      7654321  pin 4321   Kamagurka         750")

def login(bank_accounts):
    account_id = input("\nPlease enter your account id: ")
    for account in bank_accounts:
        if account.account_id == account_id:
            for attempt in range(3):
                pin = input("Enter your PIN: ")
                if account.pin_code == pin:
                    print(f"\nWelcome, {account.holder_name}")
                    return account
                else:
                     print("Invalid PIN. Please try again.")
            print("Too many failed attempts. The application will be closed.")
            exit()
    print("Invalid account id. The application will be closed.")
    exit()
bank_accounts = [BankAccount("7101968", "1234", "Danny de Vet", 1000.00), BankAccount("1234567", "4567", "Urbanus Van Anus", 500.00), BankAccount("7654321", "4321", "Kamagurka", 750.00)]

# 7101968  pin 1234   Danny de Vet  1000
# 1234567  pin 4567   Urbanus Van Anus  500
# 7654321  pin 4321  Kamagurka  750

account = login(bank_accounts)

def print_menu():
    print("\n*****************************")
    print("*****************************")
    print("**     ATM Application    ***")
    print("*****************************")
    print("*****************************")
    print(f"** Your balance: € {account.balance:.2f}  **")
    print("*****************************")
    print("1) Withdraw money")
    print("2) Deposit money")
    print("3) Exit")
    print("*****************************")
#    print("Select an option (1-3):")

while True:
    print_menu()
    keuze = input("Select an option (1-3):")
    if keuze == "1":
        amount = float(input("How much money do you want to withdraw (EUR): "))
        account.withdraw(amount)
        #print_menu()
        print(f"You withdraw €{amount:.2f}  Your new balance is: €{account.balance:.2f}")
    elif keuze == "2":
        amount = float(input("How much money do you want to deposit (EUR): "))
        account.deposit(amount)
        #print_menu()
        print(f"You deposited €{amount:.2f}  Your new balance is €{account.balance:.2f}")
    elif keuze == "3":
        print("\n     Thank you for using    ")
        print("     the ATM Application     ")
        print("*****************************")
        print("*     Shutting down ...     *")
        print("*****************************")
        break
    else:
        print("Invalid choice. Select an option (1-3):")


