sums, i = 0, 0
while True:
    x = int(input("Enter an integer (-1 to exit): "))
    if x == -1:
        print()
        print("The sum of %d number(s) is %d."%(i,sums))
        break
    else:
        sums += x
        i += 1
        print()