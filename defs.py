def list_tasks(x):
    if not x:
        print('No tasks to list')
        return
    i = 0
    print('Tasks: ')
    for values in x:
        print(f'\t [{i}] {values}')
        i += 1
    
    print()

def delete(x):
    if not x:
        print('No tasks to delete')
        return
    
    print(x)
    task_del = input('Whick task would you like to delete? [number]\n '
    '[l]for last index on the list')
    
    if task_del == 'l':
        x.pop()
        return
    int(task_del)
    if task_del.isdigit:
        # try:
        x.remove(task_del)


        # try: 
        #     x.pop()
        # except:
        #     print('errou')

     
     
    