myList = []
while True:
    x = input("Input: ")
    if x == "end":
        break
    cur, mon = x.split()
    mon = float(mon)
    if cur in ["JPY", "USD", "EUR"]:
        if mon >= 1:
            myList.append([cur,mon])
        else:
            print("ERROR")
    else:
        print("ERROR")

for i in myList:
    if i[0] == "JPY":
        con = 0.29
    elif i[0] == "USD":
        con = 31.99
    elif i[0] == "EUR":
        con = 35.62
    print("%.2f %s is %.2f THB"%(i[1],i[0],(i[1]*con)))