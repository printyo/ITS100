x = input("Input: ").split()
mydict = {}
good = True
for key in x:
    if key.isnumeric():
        if key in mydict:
            mydict[key] +=1
        else:
            mydict[key] = 1
for key, value in mydict.items():
    if good == False:
        break
    if key == str(value):
        good = True
    else:
        good = False
if good == True:
    print("Output: good sequence")
else:
    print("Output: not good sequence")