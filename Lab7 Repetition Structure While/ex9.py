count, summ = 0, 0
while True:
    x = int(input("Enter an integer (-1 to exit): "))
    print()
    if x == -1:
        print("The sum of %d number(s) is %d" % (count, summ))
        break
    else:
        count += 1
        summ += x
