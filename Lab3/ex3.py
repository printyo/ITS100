h = float(input("Enter the pentagon height: "))
a = (2*h)/((5+2*(5**0.5))**0.5)
A = (a**2*((25+10*(5**0.5))**0.5))/4
P = a *5
print("The length for one side of the pentagon is %.4f." %a)
print("The pentagon area and perimeter are %.4f and %.4f." %(A, P))