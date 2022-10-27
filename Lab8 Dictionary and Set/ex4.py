mydict = {}
while True:
    string = input("Input (DONE = exit): ")
    if string == "DONE":
        print("Output:")
        for i in sorted(mydict.values(), reverse=True):
            for j in mydict:
                if mydict[j] == i:
                    print(j,i)
        break
    key, val = string.split()
    if key.isnumeric() and val.isnumeric():
        if int(key) > 0 and int(val) > 0:
            if key in mydict:
                print("Duplicated ID")
            else:
                mydict[key] = val
    else:
        print("Invalid input")