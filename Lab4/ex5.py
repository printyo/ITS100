money = int(input("Please specify amount of money you would like to withdraw:"))
print("we may give you:")
m500 = money//500
remain = money%500
print("%d bill(s) of 500 bath"%m500)
m100 = remain//100
remain = remain%100
print("%d bill(s) of 100 bath"%m100)
m50 = remain//50
remain = remain%50
print("%d bill(s) of 50 bhat"%m50)
m2 = remain//2
remain = remain%2
print("%d coin(s) of 2 bath"%m2)
print("%d coin(s) of 1 bath"%remain)