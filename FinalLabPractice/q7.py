from operator import itemgetter
program = {"ce":0,"che":0,"ec":0,"ie":0,"me":0}
myList = []
while True:
    x = input("Input: ")
    if x == "done":
        break
    name, prog, gpa = x.split()
    gpa = float(gpa)
    if prog not in ["ce", "che", "ec", "ie", "me"]:
        print("ERROR")
    elif gpa < 0 or gpa > 4:
        print("ERROR")
    else:
        myList.append([name,prog,gpa])
        program[prog] +=1
        
print("----SUMMARY----")
for i in program.items():
    print("%s = %d"%(i[0],i[1]))
print("----LIST----")
if len(myList) == 0:
    print("The list is empty.")
else:
    for i in sorted(myList, key=itemgetter(2), reverse=True):
        print(i[0], i[1], i[2])
