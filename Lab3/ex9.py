w = float(input("Enter the width of the cube: "))
wc = float(input("Enter the width of the container: "))
hc = float(input("Enter the height of the container: "))
dc = float(input("Enter the depth of the container: "))

x = wc//w
y = hc//w
z = dc//w

print("The number of cubes that can fit into the container is %d."%(x*y*z))