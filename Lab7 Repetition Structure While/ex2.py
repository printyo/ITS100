program = True
lists = []
while program:
    x = input("Input: Enter a word:")
    if x == "exit":
        break
    else:
       lists.append(x.capitalize())
    
print("Output:", lists)