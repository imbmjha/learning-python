account_no = int(input('enter your account no: '))
name = input('enter your name: ')
balance = int(input('enter your total balance: '))
while True:
    choice = int(input('enter 1 to withdraw balance. & 2 to add balance & 3 to delete account: '))
    if choice == 1:
        print('you opt for withdraw your balance: ')
        withdraw = int(input('enter balance to withdraw: '))
        if balance >= withdraw:
            balance -= withdraw
            print('successful')
            print(f'remaining balance is {balance}')
        else:
            print('unsuccessful')
            print('unsufficient balance')
    
    elif choice == 2:
        print('you opt for add balance: ')
        deposit = int(input('enter balance to add: '))
        balance += deposit
        print(f'your new balance is {balance}')
    elif choice == 3:
        print('you opt to delete your account: ')
        withdraw = int(input(f'enter all balance {balance} to withdraw: '))
        balance -= withdraw
        print(f"your remaining balance is {balance}")
        print('successfully deleted your account')
        break
