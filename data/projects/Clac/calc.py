print("What would you like to do(X, -, /, +): ")
print("X = Times")
print("/ = Division")
print("- = Subtraction")
print("+ = Adding")

what = input("Input: ")
if what == "X":
    num1 = float(input("Num 1: "))
    num2 = float(input("Num 2: "))
    print(num1 * num2)
elif what == "-":
    num1 = float(input("Num 1: "))
    num2 = float(input("Num 2: "))
    print(num1 - num2)

elif what == "/":
    num1 = float(input("Num 1: "))
    num2 = float(input("Num 2: "))
    print(num1 / num2)

elif what == "+":
    num1 = float(input("Num 1: "))
    num2 = float(input("Num 2: "))
    print(num1 + num2)
else:
    print("Try agin")
    exit()