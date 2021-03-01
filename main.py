# Addition of   numbers
def add(num1, num2):
    return num1 + num2


# subtraction of   numbers
def subtract(num1, num2):
    return num1 - num2


#  multiplication of numbers
def multiply(num1, num2):
    return num1 * num2


# Division of numbers
def divide(num1, num2):
    return num1 / num2


print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4 :"))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if select == 1:
    print(num1, "+", num2, "=",
          add(num1, num2))

elif select == 2:
    print(num1, "-", num2, "=",
          subtract(num1, num2))

elif select == 3:
    print(num1, "*", num2, "=",
          multiply(num1, num2))

elif select == 4:
    print(num1, "/", num2, "=",
          divide(num1, num2))
else:
    print("Invalid input")

