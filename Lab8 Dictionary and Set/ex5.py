mydict = {}
sentence = input("Input a sentence: ").split()
for key in sentence:
    key = key.lower()
    if key in mydict:
        mydict[key] += 1
    else:
        mydict[key] = 1
print("Output:")
non = True
for i in mydict:
    if mydict[i] > 1:
        print(i)
        non = False
if non == True:
    print("none")