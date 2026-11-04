import numpy as np
import sys

print("\n==== SCIENTIFIC CALCULATOR ====")
print("1. ADDITION\n2. SUBTRACTION\n3. MULTIPLICATION\n4. DIVISION")
print("5. POWER\n6. SQUARE ROOT\n7. LOGARITHM\n8. LOGARITHM WITH BASE 10")
print("9. SIN\n10. COS\n11. TAN\n12. ARCSIN\n13. ARCCOS\n14. ARCTAN")

try:
    choice = int(input("Enter the choice between 1 to 14: "))
    
    if choice < 1 or choice > 14:
        print("Please enter a valid choice between 1 to 14.")
        sys.exit()

    if choice == 1:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print("SUM: ", np.add(a, b))

    elif choice == 2:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print("DIFFERENCE: ", np.subtract(a, b))

    elif choice == 3:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print("PRODUCT: ", np.multiply(a, b))  

    elif choice == 4:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        if b == 0:
            print("Cannot divide by zero!")
        else:
            print("QUOTIENT: ", np.divide(a, b)) 

    elif choice == 5:
        a = float(input("Enter the base: "))
        b = float(input("Enter the power: "))
        print("POWER: ", np.power(a, b)) 

    elif choice == 6:
        a = float(input("Enter the number: "))
        if a < 0:
            print("ERROR: Cannot calculate real square root of a negative number!")
        else:
            print("SQUARE ROOT: ", np.sqrt(a))

    elif choice == 7:
        a = float(input("Enter the number: "))
        if a <= 0:
            print("ERROR: Logarithm is only defined for numbers greater than 0!")
        else:
            print("log(x): ", np.log(a))

    elif choice == 8:
        a = float(input("Enter the number: "))
        if a <= 0:
            print("ERROR: Logarithm is only defined for numbers greater than 0!")
        else:
            print("log10(x): ", np.log10(a))

    elif choice in [9, 10, 11]:
        degree = float(input("Enter the angle in degree: "))
        angle = np.deg2rad(degree)
        if choice == 9:
            print("SIN: ", np.sin(angle))
        elif choice == 10:
            print("COS: ", np.cos(angle))
        elif choice == 11:
            print("TAN: ", np.tan(angle))

    elif choice in [12, 13]:
        a = float(input("Enter the number (between -1 and 1): "))
        if -1 <= a <= 1:
            if choice == 12:
                print("ANGLE: ", np.rad2deg(np.arcsin(a)))
            elif choice == 13:
                print("ANGLE: ", np.rad2deg(np.arccos(a)))
        else:
            print("ERROR: Value must be between -1 and 1!")

    elif choice == 14:
        a = float(input("Enter the number: "))
        print("ANGLE: ", np.rad2deg(np.arctan(a)))

except ValueError:
    print("INVALID INPUT! Please enter numeric values only!!!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")