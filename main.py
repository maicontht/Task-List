import defs
import os 
import json_defs

tasks = ['To Study Python', 'Sleep 8 hour per night']
undo_tasks = []
options = {
    '1': lambda: defs.list_tasks(tasks),
    '2': lambda: defs.delete(tasks, undo_tasks),
    '3': lambda: defs.redo(tasks, undo_tasks),
    '4': lambda: json_defs.import_list(tasks, undo_tasks),
    'add': lambda: print('hi')
}

while True:
    print('What would you like to do:\n[Enter task] = Add '
    '[1] = List tasks, [2] = Delete, [3] = Redo, [4] = Import, [5] = Export')
    
    task = input()
    os.system('cls')
    
    grab = options.get(task) if options.get(task) is not None else options['add']
    grab()
    

