import random

# Dictionary to store user data
bank_accounts = {}

def create_new_user():
    name = input("Enter your name: ")
    amount = float(input("Enter initial deposit amount: "))
    account_number = random.randint(10000, 99999)  # Generate 5-digit account number
    bank_accounts[account_number] = {'name': name, 'balance': amount}
    print(f"Account created successfully! Your account number is {account_number}")

def credit_amount():
    acc_no = int(input("Enter your account number: "))
    if acc_no in bank_accounts:
        amount = float(input("Enter amount to credit: "))
        bank_accounts[acc_no]['balance'] += amount
        print(f"Amount credited successfully! New Balance: {bank_accounts[acc_no]['balance']}")
    else:
        print("Account not found!")

def debit_amount():
    acc_no = int(input("Enter your account number: "))
    if acc_no in bank_accounts:
        amount = float(input("Enter amount to debit: "))
        if amount <= bank_accounts[acc_no]['balance']:
            bank_accounts[acc_no]['balance'] -= amount
            print(f"Amount debited successfully! New Balance: {bank_accounts[acc_no]['balance']}")
        else:
            print("Insufficient balance!")
    else:
        print("Account not found!")

def delete_account():
    acc_no = int(input("Enter your account number: "))
    if acc_no in bank_accounts:
        del bank_accounts[acc_no]
        print("Account deleted successfully!")
    else:
        print("Account not found!")

def check_info():
    acc_no = int(input("Enter your account number: "))
    if acc_no in bank_accounts:
        user = bank_accounts[acc_no]
        print(f"Name: {user['name']}, Balance: {user['balance']}")
    else:
        print("Account not found!")

def main():
    while True:
        print("APNA BANK ME AAPKA SWAGAT HAI,"
              "KARWAHI SURU KAREIN'")
        print("\n1. Existing User\n2. New User\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\n1. Credit\n2. Debit\n3. Delete Account\n4. Info Check")
            sub_choice = input("Enter your choice: ")
            if sub_choice == '1':
                credit_amount()
            elif sub_choice == '2':
                debit_amount()
            elif sub_choice == '3':
                delete_account()
            elif sub_choice == '4':
                check_info()
            else:
                print("Invalid choice!")

        elif choice == '2':
            create_new_user()
        
        elif choice == '3':
            print("Exiting... Thank you!")
            break
        
        else:
            print("Invalid choice! Please try again.")

# Run the program
main()


        

    
    
