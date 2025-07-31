import json


def read_json(x, r):
    data = []
    try:
        with open(r, 'r',encoding='utf-8') as f:
            data = json.load(f)  

    except FileNotFoundError:
        print('No file to import!')
        export_list(x)
    
    except json.decoder.JSONDecodeError:
        print('The file is empty or poorly formatted!')
        print()
        
    return data
    
def import_list():
    data = []
    try:
        with open('tasks.json', 'r',encoding='utf-8') as f:
            data = json.load(f)
            print('Tasks imported!')
            print()
            return data
        
    except FileNotFoundError:
        print('No file to import!')
        print()
        return data

    except json.decoder.JSONDecodeError:
        print('The file is empty or poorly formatted!')
        print()

        return data

def export_list(x):
    if not x:
        with open('tasks.json', 'w',encoding='utf-8') as f:
            json.dump(x, f, indent=2, ensure_ascii=False)

            print()
            return
    

    with open('tasks.json', 'w',encoding='utf-8') as f:
        json.dump(x, f, indent=2, ensure_ascii=False)

        print('Tasks imported for tasks.json!')
        print()
