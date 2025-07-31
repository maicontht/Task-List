import os

def list_tasks(x):
    if not x:
        print('No tasks to list')
        print()
        return
    
    print('Tasks: ')
    for i, value in enumerate(x):
        print(f'\t [{i}]: {value}')

    print()

def delete(x, y):
    if not x:
        print('No tasks to delete')
        print()
        return
    
    print('Tasks: ')
    for i,value in enumerate(x):
        print(f'\t [{i}]: {value}')

    task_del = input('\nWhich task would you like to delete?: [number] '
    'for a specific index [l] for last index on the list [r] to return a previous menu\n ').lower()
    
    if task_del == 'l':
        typed_value = x.pop()
        y.append(typed_value)
        os.system('cls')

        print('Tasks: ')
        for i, value in enumerate(x):
            print(f'\t [{i}]: {value}')

        print()
        return
    
    elif task_del == 'r':
        os.system('cls')

        print('Tasks: ')
        for i, value in enumerate(x):
            print(f'\t [{i}]: {value}')
        
        print()
        return
    
    elif task_del.isdigit():
        try:
            task_del = int(task_del)
            typed_value = x.pop(task_del)
            y.append(typed_value)
            os.system('cls')

            print('Tasks: ')
            for i, value in enumerate(x):
                print(f'\t [{i}]: {value}')
            print()

        except IndexError:
            os.system('cls')
            print('Index not found on the list, type a valid index!\n')
            delete(x, y)

        except OverflowError:
            os.system('cls')
            print("try typing just one command!\n")
            delete(x, y)

    else:
        os.system('cls')
        print('you typed an invalid command, type another one\n')
        delete(x, y)

def redo(x, y):
    if not y:
        print('No tasks to redo')
        print() 
        return
      
    print('Tasks: ')
    for i,value in enumerate(x):
        print(f'\t [{i}]: {value}')
    
    print()

    print('Last Tasks: ')
    for i,value in enumerate(y):
        print(f'\t [{i}]: {value}')

    task_del = input('\nWhich task would you like to redo?: [number] '
    'for a specific index [l] for last index on the list [r] to return a previous menu\n').lower()
    
    if task_del == 'l':
        last_value = y.pop()
        x.append(last_value)
        os.system('cls')

        print('Tasks: ')
        for i, value in enumerate(x):
            print(f'\t [{i}]: {value}')

        print()
        return
    
    elif task_del == 'r':
        os.system('cls')

        print('Tasks: ')
        for i, value in enumerate(x):
            print(f'\t [{i}]: {value}')
        
        print()
        return
    
    elif task_del.isdigit():
        try:
            task_del = int(task_del)
            typed_value = y.pop(task_del)
            x.append(typed_value)
            os.system('cls')

            print('Tasks: ')
            for i, value in enumerate(x):
                print(f'\t [{i}]: {value}')
            print()

        except IndexError:
            os.system('cls')
            print('Index not found on the list, type a valid index!\n')
            redo(x, y)

        except OverflowError:
            os.system('cls')
            print("try typing just one command!\n")
            redo(x, y)

    else:
        os.system('cls')
        print('you typed an invalid command, type another one\n')
        redo(x, y)

def add(x, z):
    if not z:
        print('Type something to add!')
        print()
        return
    
    z = z.strip()
    x.append(z)

    print('Tasks: ')
    for i, value in enumerate(x):
            print(f'\t [{i}]: {value}')

    print()
        