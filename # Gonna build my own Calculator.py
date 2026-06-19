# Gonna build my own Calculator

print('Welcome to the Calculator')

num1 = float(input('Enter first number: '))
operation = input('Enter operation (+, -, *, /): ')
num2 = float(input('Enter second number: '))

if operation == '+':
    result = num1 + num2
elif operation == '-':
     result = num1 - num2
elif operation == '*':
     result = num1 * num2
elif operation == '/':
     if num2 == 0:
        print("Can't divide by zero")
     else:
         result = num1 / num2
else:
        print('Invalid operation')

print('Answer:', result)
