import TerminalTellerM
import TerminalTellerC

welcome_sign = print("Welcome to Terminal Teller!:\n")

print("1) Create Account\t")
print("2) Log in to Existing Account\t")
print("3) Quit Terminal Teller\t\n")

welcome_input = input("Welcome, please enter what option you would like to proceed with:")


if welcome_input == "1":
    print('Welcome to Terminal Teller - Account Creation')
    first_name = input("Please enter first name:")
    last_name = input("Please enter last name:")
    pin = input("Please enter a 4-digit PIN number:")

    if len(pin) != 4:
        print(pin)  
        
if welcome_input == "2":
    print("Welcome to Terminal Teller - Log in/n")
    account_number = input("Please enter your personalized Account Number:/t/n")
    pin_request = input("Enter 4-digit PIN number:/t/n")
    if account_number and pin_request not in tellerdata.json:
        account_number = input("Account Number not found, please re-enter Account Number:")
        pin_request = input("Invalid PIN number, please re-enter valid PIN:")
    if account_number in "tellerdata.json":
        print(f"Hello, {first_name}({account_number})/n/n")
        print("1) Check Balance/n")
        print("2) Withdraw Funds/n")
        print("3) Deposit Funds/n")
        print("4) Sign Out/n")
        login_option = input("Option:/n")
        if login_option == 1:
            print("Account Balance is : account_balance")

if welcome_input == "3":
    print("Thanks for using Terminal Teller!")