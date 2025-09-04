print("hej! hur gammal är du?")
age = input()
age = int(age)

if age < 18:
    print("du är ett barn")
elif age == 20:
    print("du är 20")
elif age >= 18 and age < 60: 
    print("du är vuxen")

elif age >= 60:
    print("du är gammal")

else:
    print("jag vet inte vad du är")