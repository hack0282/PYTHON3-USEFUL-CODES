balance = 9000

print("welcome to STATE BANK OF INDIA")

while True:
    if input("Insert Your Card:").lower() not in {'y' or 'yes'}:
        break
    try:
        pin=(int(input('Enter A 4 Digit Number:')))
    except ValueError:
        print('Wrong Pin')
        break

    options=("""
    1: Balance Enquiry
    2: Withdraw
    3: Card To Card Transfer 
    4: Change Pin 
    5: Exit """)
    Goback=options
    print(Goback)
    choice = (int(input('Please Select any option:')))


    if choice == 1:
        print(f'your balance is {balance}')
        print(Goback)
        choice = (int(input('Please Select any option:')))
    elif choice == 2:
        amount = (int(input('Enter Your amount:')))
        if amount <= balance:
            updated_balance = balance - amount
            print(f'take your cash and your update balance is {updated_balance}')
        else:
            print("you have insufficient balance")
        break

    elif choice==3:
        try:
            card_number=(int(input('Please Enter Card Number:')))
            transfer_amount=(int(input('Enter How Much Amount To Be Transfered:')))
            if transfer_amount<balance:
                print(f'Amount {transfer_amount}is Transfered')
                print(Goback)
                choice = (int(input('Please Select any option:')))
            else:
                print('you have insufficient balance')
                print(Goback)
                choice = (int(input('Please Select any option:')))
        except ValueError:
            print('please enter 12 numeric digits only')
            break     
    elif choice==4:
            new_pin=input("enter your new pin number:")
            reenter_newpin=input("enter your new pin number:")
            if new_pin==reenter_newpin:
                print("pin changed successfully")
                break
            else:
                print("New pin dosent Match,please try to re-enter again")
                print(Goback)
                choice = (int(input('Please Select any option:')))

    elif choice==5:
        exit()

