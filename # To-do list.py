

import json

def show_menu():
    print('\n1. View tasks')
    print('2. Add task')
    print('3. Delete task')
    print('4. Exit')

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

try:
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    tasks = []

while True:
    show_menu()
    choice = input('Choose an option: ')

    if choice == '1':
        for task in tasks:
            print(task)
    elif choice == '2':
        new_task = input('Enter task: ')
        tasks.append(new_task)
        save_tasks()
    elif choice == '3':
        for i, task in enumerate(tasks):
            print(i, task)
        index = int(input('Enter number to delete: '))
        tasks.pop(index)
        save_tasks()
    elif  choice == '4':
        save_tasks()
        break
    else:
        print('Invalid choice, try again.')