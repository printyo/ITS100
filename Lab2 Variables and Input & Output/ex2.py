x = float(input("Enter x: "))
y = float(input("Enter y: "))

area_t = (x/2)*(y-(0.8*y))
area_r = (0.8*y)*(x/2)

print("Total area of the shape is %.2f square units." %(area_t + area_r))