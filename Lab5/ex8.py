print("Menu:")
print("===============")
print("A - Americano (50)")
print("E - Espresso (40)")
print("G - Green tea (60)")
print("")
order = input("Input: ")
print("===============")
count = 1
price = 0
for i in order:
  if i == "A":
    print("%d. Americano 50"%count)
    count +=1
    price += 50
  elif i == "E":
    print("%d. Espresso 40"%count)
    count +=1
    price += 40
  elif i == "G":
    print("%d. Green tea 60"%count)
    count +=1
    price += 60
  else:
    continue
print("===============")
print("Quantity: %d"%(count-1))
vat = price * 0.07
print("Vat: %.2f"%vat)
print("Total: %.2f"%price)
print("Grand total: %.2f"%(price+vat))