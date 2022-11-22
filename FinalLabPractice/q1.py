b = int(input("Enter the initial balance: "))

while True:
    x, y = input('Transaction type and amount ("done 0" to exit): ').split()
    if x == "done" and y == '0':
        print("> Current Balance = %d THB"%b)
        break
    y = int(y)
    if x == "D" and y > 0:
        b += y
        print("> Deposit = %d THB, current balance = %d THB"%(y,b))
    elif x == "W" and y <= b:
        b -= y
        print("> Withdraw = %d THB, current balance = %d THB"%(y,b))
    else:
        print("> Invalid transaction!")