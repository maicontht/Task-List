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
    task_del = input('Whick task would you like to delete? [number]\n '
    '[l]for last index on the list [r] to return a  previous menu ').lower()
    
    
    if task_del == 'l':
        x.pop()
        return
    
    elif task_del == 'r':
        x.pop()
        return
    
    elif task_del.isdigit():
        try:
            task_del = int(task_del)
            x.pop(task_del)

        except IndexError:
            print('Index not found on the list, type a valid index!')

    else:
        print('you typed an invalid command, type another one')

     
     
    