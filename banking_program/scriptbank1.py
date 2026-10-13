import random

def show_balance(balance):
    print(f"Your current balance is {balance:.2f}.")
    return balance

def deposit(balance):
    depositing = False
    while not depositing:
     deposit_amount = float(input(f"How much do you want to deposit?(type: '0' to exit)::-> "))
     if deposit_amount > 500:
         print("Sorry, you can't deposit more than $500 at once")
     elif deposit_amount < 0:
              print("You can't choose a negative value")
     elif deposit_amount == 0:
         break
     else:
         print(f"You succesfully deposited {deposit_amount} in your bank account")
         balance = balance + deposit_amount
         show_balance(balance)
         depositing = True
    return balance

def withdrawal(balance):
    withdrawing = False
    while not withdrawing:
        withdrawal_amount = float(input(f"How much do you want to withdraw? (type: '0' to exit)::-> "))
        if withdrawal_amount > 500:
            print("Sorry, you can't withdraw more than 500 at once")
        elif withdrawal_amount == 0:
            break
        elif withdrawal_amount < 0:
                    print("You can't choose a negative value")
        elif balance < withdrawal_amount:
            print(f"Unfortunately, your current balance is {balance}.")
        else:
            withdrawing = True
            print(f"You succesfully withdrew {withdrawal_amount} from your bank account")
            balance = balance - withdrawal_amount
            show_balance(balance)
    return balance

def main():
    import random
    
    balance = round(random.uniform(-10000,100000), 2)
    is_running = True
    access_ok = False

    print("*"*5,"Welcome to our Mobile Bank App","*"*5)

    while not access_ok:

        email = input("Type here your email address to access your profile:-> ").strip()
        email_divided = email.split("@")

        if not email.count("@") == 1:
            print("Please insert a valid email to access...")

        elif email.count(" ") > 0:
            print("Please insert a valid email to access...")

        elif len(email_divided[0]) == 0:
            print("Please insert a valid email to access...")

        elif len(email_divided[1]) == 0:
            print("Please insert a valid email to access...")

        else:
            access_ok = True
            print("Email is valid!")
            print()
    
    print("*"*5, "How can we help you today?", "*"*5)

    while is_running:
        print("TYPE:\n1) Balance: to check your current balance;\n2) Deposit: if you want to make a deposit;\n3) Withdrawal: if you want to withdraw money;\n-- (type: 'leave' to exit)")
        action = input("Your choice:-> ").lower().strip()
        match action:
            case "2":
                balance = deposit(balance)
            case "3":
                balance = withdrawal(balance)
            case "1":
                balance = show_balance(balance)
            case "leave":
                is_running = False
            case __:
                print("Please type a valid value!")
    
if __name__ == "__main__":
    main()
    


