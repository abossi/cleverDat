import re
import pickle

func = ["imp"]

#parameters:
#file | '' = file
#line_sep | '\n' = str
#col_sep | ';' = str
#header | False = bool

parameters = {
    'file': {
        'value': "",
        'type': 'str'
    },
    'line_sep': {
        'value': "\\n",
        'type': 'str'
    },
    'col_sep': {
        'value': ";",
        'type': 'str'
    },
    'header': {
        'value': False,
        'type': 'bool'
    }
}

def plugin(id, **dic):
    def decorator(func):
        def wrapper(*args):
            tmp = pre(id, *args, **dic)
            data = func(*args)
            post(**dic)
            if args[1] == -1 or args[1] < id:
                data.insert(0, tmp)
                return data
            elif args[1] == id:
                return tmp
            return data
        return wrapper
    return decorator

def pre(id, *args, **dic):
    print("read csv " + dic['file'])
    result = {}
    if dic['file'] == '':
        return {'message': 'No file selected!'}
    try:
        if args[1] != id:
            with open(dic['file'] + dic['line_sep'] + dic['col_sep'] + str(dic['header']) + '.pkl', 'rb') as input:
                return {dic['file']: pickle.load(input)}
    except FileNotFoundError:
        pass
    try:
        with open(dic['file'], 'r') as csvfile:
            data = ''
            if args[1] == id:
                data = csvfile.read().split(dic['line_sep'], 21)[:21]
            else:
                data = csvfile.read().split(dic['line_sep'])
            data = [re.sub('"', '', x).split(dic['col_sep']) for x in data]
            length = len(data[0])
            data = [x for x in data if len(x) == length]
            headers = []
            if dic['header']:
                headers = data[0]
                data = data[1:]
            list_csv = data
            if not len(headers):
                headers = [i for i in range(len(list_csv[0]))]
            list_csv = list(map(lambda *a: list(a), *list_csv))
            for i,el in enumerate(headers):
                if i < len(list_csv):
                    result[el] = list_csv[i]
    except FileNotFoundError:
        return {'message': "Don't forget to upload the file on the server!"}
    if args[1] != id:
        with open(dic['file'] + dic['line_sep'] + dic['col_sep'] + str(dic['header']) + '.pkl', 'wb') as output:
            pickle.dump(result, output, pickle.HIGHEST_PROTOCOL)
    return {dic['file']: result}




def post(**dic):
    return {}

def API(func):
    def wrapper(*args):
        func(*args)
    return wrapper
