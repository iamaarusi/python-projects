balance = 1000
pin = "1234"

def check_balance():
    print("Current Balance:", balance)

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Amount Deposited Successfully")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))

    if amount <= balance:
        balance -= amount
        print("Withdrawal Successful")
    else:
        print("Insufficient Balance")

user_pin = input("Enter PIN: ")

if user_pin == pin:

    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("Thank You for Using ATM")
            break

        else:
            print("Invalid Choice")

else:
    print("Incorrect PIN")