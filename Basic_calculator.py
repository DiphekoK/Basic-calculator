print("------------Basic Calculator--------------")

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
operation = input("Multiplication(*),Division(/),Addition(+) or Subtraction(-): ")

if operation == "*":
    result = num1 * num2
    print(num1,operation,num2,"=",result)
elif operation == "/":
    result = num1 / num2
    print(num1,operation,num2,"=",result)
elif operation == "+":
    result = num1 + num2
    print(num1,operation,num2,"=",result)
elif operation == "-":
    result = num1 - num2
    print(num1,operation,num2,"=",result)
