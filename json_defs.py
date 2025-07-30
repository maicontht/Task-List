import json

# def read_json():


    
#def import_list(x, y): 
 #   with open('tasks.json', 'r',encoding='utf-8') as f:
  ##     print(list_json)

def export_list(x, y):
    if not x:
        print('No tasks for export!')
        print()
        return

    with open('tasks.json', 'w',encoding='utf-8') as f:
        json.dump(x, f, indent=2, ensure_ascii=False)

    with open('undo_tasks.json', 'w',encoding='utf-8') as f:
        json.dump(y, f, indent=2, ensure_ascii=False)

    print('Tasks imported for tasks.json!')
    print()

