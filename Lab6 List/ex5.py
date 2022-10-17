n = int(input("How many persons in a group? : "))
a,b,c = [],[],[]
print("Please enter grade from group A")
for i in range(n):
  x = float(input("enter grade: "))
  a.append(x)
print("Please enter grade from group B")
for i in range(n):
  x = float(input("enter grade: "))
  b.append(x)
print("Please enter grade from group C")
for i in range(n):
  x = float(input("enter grade: "))
  c.append(x)
print("the highest grade of group A is %.1f"%(max(a)))
print("the highest grade of group B is %.1f"%(max(b)))
print("the highest grade of group C is %.1f"%(max(c)))