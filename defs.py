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
    
    
    for i,value in enumerate(x):
        print(f'\t [{i}]: {value}')
    task_del = input('Whick task would you like to delete? [number]\n '
    '[l]for last index on the list' )
    
    if task_del == 'l':
        x.pop()
        return
    
    if task_del.isdigit:
        try:
            task_del = int(task_del)
            x.pop(task_del)
        except ValueError:
            print("Digite um numero valido")

        # try: 
        #     x.pop()
        # except:
        #     print('errou')

     
     
    