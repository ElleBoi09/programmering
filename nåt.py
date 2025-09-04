print("Hur gammal är du?")
age = input()
age = int(age)
if age <= 14:
    print("du ska ha barnbiljett för 16kr")
elif age >= 15 and age <=20:
    print("du ska ha ungdomsbiljett för 20kr")   
elif age >=20 and age <=65:
    print("du ska ha ordinariebiljett för 27kr")