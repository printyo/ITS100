digit4 = input("Enter a four-digit integer: ")

first = int(digit4[:2])
last = int(digit4[2:])

print("The result of %d + %d = %d"%(first,last,(first+last)))
print("The result of %d - %d = %d"%(first,last,(first-last)))
print("The integer value of %d/%d = %d"%(first,last,(first//last)))
print("The remainder of %d/%d = %d"%(first,last,(first%last)))