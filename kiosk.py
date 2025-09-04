print(" hej! Välkommen till kiosken! Det finns 4 olika val som du kan betala för att få! Vilken/vilka blir det?")
print("glass = 20kr") 

print("varmkorv = 15kr") 

print("läsk = 15kr")

print("godis = 10kr")

item = input()

if item == "glass":
    print("hur många vill du ha?")
    amount = input()
    amount = int(amount)
    cost = amount * 20
    print("det kostar",cost,"kr")

elif item == "varmkorv":
    print("hur många vill du ha?")
    amount = input()
    amount = int(amount)
    cost = amount * 15
    print("det kostar",cost,"kr")


elif item == "läsk":
    print("hur många vill du ha?")
    amount = input()
    amount = int(amount)
    cost = amount * 15 
    print("det kostar",cost,"kr")

elif item == "godis":
    print("hur många vill du ha?")
    amount = input()
    amount = int(amount)
    cost = amount * 10
    print("det kostar",cost,"kr")