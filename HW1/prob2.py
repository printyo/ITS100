cost = float(input("Input the cost of a meal: "))
service = cost * 0.1
print("Service charge = %.2f THB" %service)
vat = (cost + service) * 0.07
print("VAT = %.2f THB"%vat)
print("Total cost = %.2f THB"%(cost+service+vat))