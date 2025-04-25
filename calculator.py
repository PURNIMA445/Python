import sys
calculation_history = []
def divide(a,b):
    if (b==0):
        print("Infinte valuee")
    else:
        calculation_history.append(f"divide({a},{b}={a/b})")
        return a/b
def multiply(a,b):
    calculation_history.append(f"Multiply({a},{b}={a*b})")
    return a*b
def addition(a,b):
    calculation_history.append(f"addition({a},{b}={a+b})")
    return a+b
def subtraction(a,b):
    calculation_history.append(f"add({a},{b}={a-b})")
    return a-b
def sqroot(a):
    calculation_history.append(f"Sqrt{a}={a**(1/2)})")
    return a**(1/2)
def power(a,b):
    calculation_history.append(f"power({a}^{b}={a^b})")
    return a**b 
def number():
    print("enter two numbers:")
    x,y=int(input()),int(input())
    return x,y
def options():
    print("Choose the operators")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Square root")
    print("6. Power")
    print("7. History logs")
    print("8. Exit")
while True:
    options()
    choice=int(input("Enter the number from (1-8)"))
    try:
        match int(choice):
            case 1:
                x,y=number()
                value=addition(x,y)
                print(f"Addition of {x} and {y} is {value}")
            case 2:
                x,y=number()
                print(f"Subtraction of {x} and {y} is {subtraction(x,y)}")
            case 3:
                x,y=number()
                print(f"{x} divided by {y} is {divide(x,y)}")
            case 4:
                x,y=number()
                print(f"{x} multiplied by {y} is {multiply(x,y)}")
            case 5:
                a=float(input("Enter a number"))
                print(f"Square root of {a} is {sqroot(a)}")
            case 6:
                x,y=number()
                print(f"{x} ^ {y} is {power(x,y)}")
            case 7:
                for entry in calculation_history:
                    print(entry)
            case 8:
                sys.exit()
            case _:
                print("INVALID NUMBERRRRR!!!!!!!!")
    except ValueError:
        print("Please enter numbers only!")


