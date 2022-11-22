while True:
    n = int(input("Enter an integer number (0 to exit): "))
    if n < 0 or n > 9:
        print("Valid value is between 0 and 9!")
        break
    elif n == 0:
        print("Exit program. Bye!")
        break
    else:
        for i in range(1,n+1):
            print(" "*(n-i), end='')
            print(("%s "%n)*i)