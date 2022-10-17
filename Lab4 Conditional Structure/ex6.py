print("===============================")
x = float(input("Input x = "))
y = float(input("Input y = "))

alpha = ((0-2)*(x-1)+(1-2)*(y-2))/((0-2)*(0-1)+(1-2)*(0-2))
beta = ((2-0)*(x-1)+(0-1)*(y-2))/((0-2)*(0-1)+(1-2)*(0-2))

gamma = 1- alpha - beta

if alpha > 0 and beta > 0 and gamma > 0:
  print("Point(x,y) inside polygon")
else:
  print("Point(x,y) outside polygon")