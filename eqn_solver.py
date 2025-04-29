import cmath  
import numpy as np 
def quadratic():
    print("\n--- Solving Quadratic Equation (ax^2 + bx + c = 0) ---")
    a = int(input("Enter value of a (a ≠ 0): "))
    b = int(input("Enter value of b: "))
    c = int(input("Enter value of c: "))
    d = (b ** 2) - (4 * a * c)  # Calculate discriminant
    root1 = (-b - cmath.sqrt(d)) / (2 * a)
    root2 = (-b + cmath.sqrt(d)) / (2 * a)
    print(f"The roots of the equation {a}x^2 + {b}x + {c} are: {root1} and {root2}")


def linear():
    print("\n--- Solving Linear Equation (ax + b = 0) ---")
    a = int(input("Enter value of a (a ≠ 0): "))
    b = int(input("Enter value of b: "))
    
    x = -b / a  # Solve for x
    print(f"The value of x is: {x}")

# Function to solve 2 linear equations with 2 variables
def multi_linear():
    print("\n--- Solving Two Linear Equations with Two Variables ---")
    print("Equation 1: ax + by = c")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    print("\nEquation 2: dx + ey = f")
    d = float(input("Enter d: "))
    e = float(input("Enter e: "))
    f = float(input("Enter f: "))

    # Create coefficient matrix A and constant vector B
    A = np.array([[a, b], [d, e]])
    B = np.array([c, f])

    try:
        # Solve the system A·X = B
        X = np.linalg.solve(A, B)
        print("\nSolution:")
        print("x =", X[0])
        print("y =", X[1])
    except np.linalg.LinAlgError:
        print("No unique solution exists (the lines may be parallel or identical).")

while True:
    print("\nChoose the type of equation you want to solve:")
    print("1. Quadratic Equation (ax^2 + bx + c = 0)")
    print("2. Linear Equation (ax + b = 0)")
    print("3. Two Linear Equations with Two Variables")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        quadratic()
    elif choice == '2':
        linear()
    elif choice == '3':
        multi_linear()
    elif choice == '4':
        print("Exiting the program. Bye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")