#Welcome to Bhatacharya Bank:
#Where invoices are not just numbers, they are emotions.
#Where inovation is our tradition.

#Bank Management System
import random #Importing random module
import json
import time

Bank_Manager="Mr Smarak Acharya"
amount = 0
minimum_balance = 5000
name = []
account_number = []
balance = balance =(float)
accounts = {}
pin_code = []
choose = 0
increment = 1.2
time_interval=15
accounts={}

#All the functions:
def saving_accounts_diffrently(): #Saving files function
    try:
        with open('accounts.json', 'w') as storage:
            json.dump(accounts, storage)
    except Exception as e:
        print(f"An error occuerred while saving accounts: {e}")
def save_accounts_to_file(): #Saving files function
    try:
        with open('joke.json', 'w') as storage:
            json.dump(accounts, storage)
    except Exception as e:
        print(f"An error occuerred while saving accounts: {e}")

def load_accounts_from_jsonfile():  # Loading files function
    global accounts
    try:
        with open('joke.json', 'r') as storage:
                accounts = json.load(storage)
    except json.JSONDecodeError:
        print("Error decoding JSON from file.")
        accounts = {}
    except Exception as e:
        print(f"An error occurred while loading accounts: {e}")
        accounts = {}

load_accounts_from_jsonfile() #Loading files

       
def Functionality():
    while True:
        print("\nWelcome to Bhatacharya Bank:")
        print('''
        Where invoices are not just numbers, they are emotions.
        Where inovation is our tradition.")
        Where your money is safe and secure.")
        Where your trust is our pride and priority.")
        Where your satisfaction is our success.")
        Where the value of zero is not just a number, its the starting point from where, the journey to the infinite success and inovations beings")
        \nPlease Enter 1.If You want to make any kind of transactions
        Please Enter 2.If You want to check balance in your Bank Account
        Please Enter 3.If You want to create a Bank Account in our Bhatacharya Bank
        Please Enter 4.If You want to change your Bank Account Pin
        Please Enter 5.IF You want to Exit the Bank Service Menu''')
        choose = int(input("Please Enter the Number of the option you want to choose: "))
        if choose == 1:
            print("\nWelcome to Bhatacharya Bank Transaction Service: ")
            print("Please Enter 1.If you want to Diposite Money into your Bank Account")
            print("Please Enter 2.If you want to Withdraw Money from your Bank Account")
            choice =int(input("Please Enter Your Choosed Option Number: "))
            if choice == 1:
                deposit()
                break
            else:
                ("Opps Something Went Wrong")
            if choice == 2:
                withdraw()
                break
            else:
                ("Opps Something Went Wrong")
        elif choose == 2:
            print("\nWelcome to Bhatacharya Bank Check-in Service")
            check_balance()
            break
        elif choose == 3:
            print("\nWelcome to Bhatacharya Bank Account Management Service")
            create_account()
            break
        elif choose == 4:
            print("\nWelcome to Bhatacharya Bank Account Managemnet Service")
            change_pin()
        elif choose == 5:
            print("\nThank You For Visiting And Using Our Bank Service")
            print("Have a good day Sir/Mam")
            break
        elif choose == 8917589592:
            print(f"Welcome Manager{Bank_Manager} To the Bhatacharya Controling Service ")
            A=int(input("Enter 1.To Access Accounts in Bank 2.To Access Account Numbers and Info"))
            if A == 1:
                print(accounts)
            elif A == 2:
                print(accounts(account_number))
                break
            else:
                print("Wrong Input")
        else:
            print("Invalid Input")
            break
        pass


def account_number_generator():#generating account number
    while True:
        account_number = random.randint(1000000000, 9999999999)
        account_number = str(account_number)
        return account_number

def pin_code_generator():#generating pin code
    while True:
        pin_code = random.randint(1000, 9999)
        pin_code= int(pin_code)
        return pin_code

def create_account():#creating account
    while True:
        name = str(input("Enter your name: "))#INFO Required
        gender= str(input("Enter your genter male/female: "))
        balance = float(input("Enter amount you want to deposite into your new account: "))#first deposite
        if balance<minimum_balance:
            print("Minimum balance should be 5000")
            balance = float(input("Enter your balance: "))
            continue
        else:
            account_number = account_number_generator()
            pin_code = pin_code_generator()
            accounts[account_number] ={
                'name': name,
                'gender':gender,
                'balance': balance,
                'pin': pin_code
            }
            if gender.lower() =="male":
                print("Hello Mr_", name)
                name = (f"Mr_{name}")
                accounts[account_number]['name'] = name

            elif gender.lower()=="female":
                print("Hello Mrs.", name)
                name = (f"Mrs_{name}")
                accounts[account_number]['name'] = name

            if gender =="Male":
                print("Hello Mr_", name)
                name = (f"Mr_{name}")
                accounts[account_number]['name'] = name
            
            elif gender =="Female":
                print("Hello Mrs_", name)
                name = (f"Mrs_{name}")
                accounts[account_number]['name'] = name

            print("Account Number: ", account_number)
            print("Pin Code: ", pin_code)
            print("Balance: ", balance)
            print("Account Created Successfully")
            save_accounts_to_file()
            saving_accounts_diffrently()
            break
    pass 

def withdraw():#Withdraw function
    while True:
        account_number= input("Enter your account number: ")#account no.
        if account_number not in accounts:#account no.check 1
            print("Looks like you don't have a Bank Account in our Bhatacharya Bank")
            answer=input("Do you want to create a Bank Account in our Bhatacharya Bank Enter (yes/no): ")
            if answer.lower()=='yes':
                create_account()
                break
            else:
                print("Thank You For Using our Bank System")
                break

        elif account_number in accounts:#check 2 with elif argument
            pin_code = int(input("Enter your pin code: "))#secutity pin

            if accounts[account_number]['pin'] == pin_code:#Pin check 1
                balance= accounts[account_number]['balance']
                name= accounts[account_number]['name']
                amount = float(input("Enter amount to be withdrawn: "))

            
                
                if balance > amount and balance > minimum_balance:#Checking ammount in account check 2 with elif argument
                    balance = balance - amount
                    accounts[account_number]['balance'] = balance
                    print("You Withdrew:", amount)
                    print("Your balance is now: ", balance)
                    print("Your Transaction was Successful")
                    save_accounts_to_file()
                    break

                elif balance <= amount or balance >=amount and balance < minimum_balance:#Checking 2 
                    print("Insufficient balance")
                    print("Your balance is: ", balance)
                    print("You can withdraw only from", balance)
                    answer=input("Do you want to withdraw any other amount? (yes/no)")
                    if answer.lower() == "yes":

                        amount=float(input("Enter amount to be withdrawn"))#New amount


                        if balance > amount and balance > minimum_balance:#Checking New amount
                            balance = balance - amount
                            accounts[account_number]['balance'] = balance
                            print(name," You Withdrew:", amount)
                            print(name,"Your Balance is now:", balance)
                            print("Your Transaction was Successful")
                            save_accounts_to_file()
                            break

                        elif balance <= amount or balance >=amount and balance < minimum_balance:#Checking 2
                                print("Bank account minimum balance is going to be less than 5000 according to bank the minimum mainained balanace must be 5000")
                                print("You cannot withdraw this amount", amount)
                                print("If you still want to withdraw, there will be a penalty of 2500 from the bank")
                                answer= input("Do you still want to withdraw? (yes/no)")
                                if answer.lower() == "yes":
                                    balance=balance-amount
                                    balance=balance-2500
                                    accounts[account_number]['balance'] = balance #updating the value of balance
                                    print(name,"You Withdrew:", amount)
                                    print(name,"Your balance now is: ", balance)
                                    print("Your Transaction was Successful")
                                    save_accounts_to_file
                                    break
                                if answer.lower() =="no":
                                    print("Transaction canceled")
                                else:
                                    print("Tansaction failed")
                                    break
                        else:
                            print("Transaction failed")
                            break
                    else:
                        print("Transaction failed")
                elif accounts[account_number]['pin'] !=pin_code:#Pin check 2 with elif argument
                    print("Your pin is wrong")
                    answer=input("Do You want to change your Bank Account Pin Enter (yes/no): ")#change pin function
                    if answer.lower()=='yes':
                        change_pin()
                    else:
                        print("Transaction canceled")
                    break 
                else:
                    print("Transaction failed")
                    break
            else:
                print("Transaction failed")
                break
        else:
            ("Transaction failed")
            break
        pass
    

def deposit():#Deposite function
    while True:
        account_number = input("Enter your account number: ")#account no.

        if account_number not in accounts:#Checking account no.
            print("Looks like you doesn't have a Bank Account in our Bhatacharya Bank")
            answer=input("Do You want to create a Bank Account in our Bhatacharya Bank Enter (yes/no): ")
            if answer.lower() =='yes':
                create_account()
                break
            else:
                print("Thank You For Using our Bank System")
                break

        if account_number in accounts:#Checking 2
                pin_code = int(input("Enter your pin code: "))#Security pin

        if accounts[account_number]['pin'] == pin_code:#pin check 1
                name = accounts[account_number]['name']
                balance = accounts[account_number]['balance']
                amount = float(input("Enter amount to be deposited: "))
                balance = balance + amount
                accounts[account_number]['balance'] = balance #updating the value of blanace
                print("\nAmount Deposited:", amount)
                print(name,"Your balance is: ", balance)
                print("Your Transaction was Successful")
                save_accounts_to_file()
                break
        elif accounts[account_number]['pin'] != pin_code:#pin check 2
            print("Your pin is wrong")
            answer=input("If You want to change your Pin Enter (yes/no): ")
            if answer.lower() =='yes':
                    change_pin()
                    break
            else:
                print("Transaction canceled")
                break
        else:
            print("Transaction failed")
            break
    pass


def check_balance():#Balance checking functions
    while True:
        account_number = input("Enter your account number: ")#account no.

        if account_number not in accounts:#Checking account no.
            print("Looks like you doesn't have a Bank Account in our Bhatacharya Bank")
            answer= input("Do you want to creaate a Bank Account in our Bhatacharya Bank Enter (yes/no): ")
            if answer.lower() =='yes':
                create_account()
                break
            else:
                print("Thank You For Using our Bank System")
                break

        elif account_number in accounts:#Check 2
            pin_code = int(input("Enter your pin code: "))#Security pin

            if accounts[account_number]['pin'] == pin_code:#pin checking
                balance = accounts[account_number]['balance']
                name = accounts[account_number]['name']
                print(name,"Your balance is: ", balance)
                break
            elif accounts[account_number]['pin']!=pin_code:#Checking 2
                print("Your pin is wrong")
                answer = input("If You want to change your Bank Account Pin Enter (yes/no): ")
                if answer.lower()=='yes':
                    change_pin()
                    break
                else:
                    print("Thank You For Using our Bank System")
                    break
            else:
                print("Transaction failed")
        else:
            print("Transaction failed")
        pass

def change_pin():#Change pin function
    while True:
        account_number = input("Enter your account number: ")#account no.

        if account_number not in accounts:#Checking account no. 1
            print("Looks like you don't have a Bank Account in our Bhatacharya Bank")
            answer = input("Do You want to create a Bank Account in our Bhatacharya Bank (yes/no): ")
            if answer.lower() =='yes':
                create_account()
                break
            else:
                print("Thank You For Using our Bank System")
                break

        elif account_number in accounts:#Checking 2
            name=input('Please enter your name: ')#Name for clarity

            if name in accounts[account_number]['name']:#Name Validation 1
                new_pin = int(input("Enter new pin code: "))#New security pin
                accounts[account_number]['pin'] = new_pin
                print(name,"Your Pin code has been changed successfully")
                save_accounts_to_file()
                break

            elif name not in accounts[account_number]['name']:#Validation 2
                print("Your name is not in our records")
                answer= input("Want to create a account? (yes/no)")
            if answer.lower() =="yes":
                create_account()
                break
            else:
                print("Thank you")
                break
        else:
            print("Some Technical Error Has Occured")
            print("Sorry for the inconvenience")
            print("please try again later")
            print("Thank you")
        pass

def main():
        while True:
            time.sleep(time_interval)
            for account_number in accounts:
                balance = accounts[account_number]['balance']
                print(f"Current balance for account {account_number}: {balance}")
                accounts[account_number]['balance'] = balance + (balance * increment)
            save_accounts_to_file()
            saving_accounts_diffrently()
            Functionality()
                       

if __name__ == "__main__":
    main()
