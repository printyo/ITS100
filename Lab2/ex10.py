its = float(input("enter grade from ITS100: "))
el = float(input("enter grade from EL171: "))
scs = float(input("enter grade from SCS183: "))

avg = ((its * 3) + (el * 3) + scs)/7
print(" ")
print("Your GPA is %.2f" %avg)