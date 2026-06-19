# while loop
num = int(input('Enter a number between 1 and 10: '))

while num < 1 or num > 10:
    print(f'{num} is not between 1 and 10. Please try again.')
    num = int(input('Enter a number between 1 and 10: '))

print(f'You entered {num}, which is between 1 and 10. Thank you!')