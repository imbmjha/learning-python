balance = int(input('enter balance= '))
while True:
    mobile = int(input('enter your no= '))
    recharge_amount = int(input('enter your recharge amount='))
    

    if balance > recharge_amount:
        balance = balance - recharge_amount
        print('recharge successful')
        print(f'your remaining balance is {balance}')
    else:
        print('unsuccessful')
        print('your balance is low')
        break