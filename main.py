import defs
import os 
import json_defs


path_json = 'tasks.json'
tasks = json_defs.read_json([], path_json)
undo_tasks = []
options = {
    '1': lambda: defs.list_tasks(tasks),
    '2': lambda: defs.delete(tasks, undo_tasks),
    '3': lambda: defs.redo(tasks, undo_tasks),
    '4': lambda: tasks.extend(json_defs.import_list()),
    '5': lambda: json_defs.export_list(tasks),
    'add': lambda: defs.add(tasks, task)
}

print('Tasks: ')
for i, value in enumerate(tasks):
    print(f'\t [{i}]: {value}')

print()

while True:
    print('What would you like to do:\n[Enter task] = Add '
    '[1] = List tasks, [2] = Delete, [3] = Redo, [4] = Import, [5] = Export')
    
    task = input()
    os.system('cls')
    
    grab = options.get(task) if options.get(task) is not None else options['add']
    grab()
    

