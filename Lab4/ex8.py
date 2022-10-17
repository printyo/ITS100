print("welcome to pizza online ordering.")
print('please input "y" if you want to order, otherwise input "n"')
pizza = input("pizza? (price_359): ")
chicken = input("chicken? (price_3 pieces for 199): ")
pasta = input("pasta? (price_99): ")
salad = input("salad? (price_99): ")
coke = input("coke? (price_550 ml for 25): ")

total = 0
if pizza == "y":
  total += 359
if chicken == "y":
  total += 199
if pasta == "y":
  total += 99
if salad == "y":
  total += 99
if coke == "y":
  total += 25
print("total price is %d"%total)
print("thanks")