def LeftRotate(x,n):
    for i in range(n):
        a = x[0]
        del x[0]
        x.append(a)
    return x

def RightRotate(x,n):
    for j in range(n*2):
        a = x[4]
        del x[4]
        x.insert(0,a)
    return x

lis = input("Enter 5 inputs: ").split()
try:
    n = int(input("Enter an integer number of rotation (0-4): "))
except ValueError:
    print("Error!")
else:
    if 0 <= n <= 4:
        print("The left-rotated list:", LeftRotate(lis,n))
        print("The right-rotated list:", RightRotate(lis,n))
    