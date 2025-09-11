print("Välj två nummer!")
number_1 = input()
number_1 = int(number_1)

number_2 = input()
number_2 = int(number_2)

def addition(x,y):
    return x+y

def subtraction(x,y):
    return x-y 

def multiplication(x,y):
    return x*y 

def division(x,y):
    return x/y 

print("Vad vill du göra?")
print("addition")
print("subtraction")
print("multiplication")
print("division")

choice = input()

if choice == "addition":
    result = addition(number_1, number_2)
    print(result)
elif choice == "subtraction":
    result = subtraction(number_1, number_2)
    print(result)

elif choice == "multiplication":
    result = multiplication(number_1, number_2)
    print(result)

elif choice == "division":
    result = division(number_1, number_2)
    print(result)