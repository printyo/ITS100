program = True
lists = []
while program:
    x = input("Input: Enter a word:")
    if x == "exit":
        break
    else:
        if x[-1] == "y":
            x = x[:-1]
            x += "ily"
            lists.append(x)
        else:
            lists.append(x)
    
print("Output:", lists)