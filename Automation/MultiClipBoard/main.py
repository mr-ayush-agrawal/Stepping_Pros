import sys
import json
import clipboard as cb
FILE_LOC = 'Clipboard.json'

def load_items():
    try:
        with open(FILE_LOC, 'r') as f:
            data = json.load(f)
            return data
    except:
        return {}

def save(cb_data):
    def save_items(data):
        with open(FILE_LOC, 'w') as f:
            json.dump(data,f)
    
    key =  input('Enter a key to save the data: ')
    cb_data[key] = cb.paste()
    save_items(cb_data)
    print('Data Saved')


def load(data):
    key =  input('Enter a key to save the data: ')
    if key in data:
        cb.copy(data[key])
        print('Data Copied to clip board')
    else :
        print('Given Key does not exist')


def list(data):
    print(data)


if __name__ =='__main__':
    if (len(sys.argv) == 2):
        comand = sys.argv[1]
        data = load_items()

        if comand in ['SAVE', 'save', 'Save'] :
            save(data)
        elif comand in ['LOAD', 'Load', 'load']:
            load(data)
        elif comand in ['LIST', 'List', 'list']:
            list(data)
        else:
            print('Unknown Command')
        
        print('\n',sys.argv[0])
            
    else :
        print('Please Pass only 1 command at a time')