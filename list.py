numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Bananas', 'Cherrys' , 'Grapes'] #list of strings-=

numbers2 = list((1, 2, 3, 4, 5))
fruits2 = list(('Apples', 'Bananas', 'Cherrys'))

#print(numbers, numbers2)


# Get a value
print(fruits[3])

# Get length
print(len(fruits))

# Append to list
fruits.append('Oranges')

fruits.remove('Bananas')

print(fruits)
