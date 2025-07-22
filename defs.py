import os

def list_tasks(x):
    if not x:
        print('No tasks to list')
        return
    
    print('Tasks: ')
    for i, value in enumerate(x):
        print(f'\t [{i}]: {value}')
       
    print()

def delete(x):
    if not x:
        print('No tasks to delete')
        return
    
    print('Tasks: ')
    for i,value in enumerate(x):
        print(f'\t [{i}]: {value}')

    task_del = input('\nWhich task would you like to delete?: [number] '
    'for a specific index [l] for last index on the list [r] to return a previous menu ').lower()
    
    if task_del == 'l':
        x.pop()
        os.system('cls')
        print('Tasks: ')
        for i, value in enumerate(x):
            print(f'\t [{i}]: {value}\n')
        return
    
    elif task_del == 'r':
        os.system('cls')
        print('Tasks: ')
        for i, value in enumerate(x):
            print(f'\t [{i}]: {value}\n')
        return
    
    elif task_del.isdigit():
        try:
            task_del = int(task_del)
            x.pop(task_del)
        except IndexError:
            os.system('cls')
            print('Index not found on the list, type a valid index!\n')
            delete(x)
        except OverflowError:
            os.system('cls')
            print("try typing just one command!\n")
            delete(x)

    else:
        os.system('cls')
        print('you typed an invalid command, type another one\n')
        delete(x)

     
     
    