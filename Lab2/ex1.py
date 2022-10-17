chocolate = int(input("Enter amount of melted chocolate to be poured into the cup (ml): "))
milk = int(input("Enter amount of milk to be poured into the cup (ml): "))

total = chocolate + milk
oz = total * 0.0338

print("Now Emmy's cup is filled with %.2f ml (or about %.2f oz) of chocolate milk." %(total,oz))