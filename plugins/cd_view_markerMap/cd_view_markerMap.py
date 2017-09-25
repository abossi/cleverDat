import csv

func = ["exp"]

parameters = {
    'table': {
        'value': "",
        'type': 'str'
    },
    'longitude': {
        'value': "",
        'type': 'str'
    },
    'latitude': {
        'value': "",
        'type': 'str'
    },
    'popup': {
        'value': "",
        'type': 'str'
    }
}

def plugin(id, **dic):
    def decorator(func):
        def wrapper(*args):
            if args[1] == id:
                return pre(*args, **dic)
            return func(*args)
        return wrapper
    return decorator

def pre(*args, **dic):
    result = []
    for table in args[2]:
        if dic['table'] in table.keys():
            if dic['popup'] in list(table[dic['table']].keys()):
                result = [table[dic['table']][dic['latitude']], table[dic['table']][dic['longitude']], table[dic['table']][dic['popup']]]
            else:
                result = [table[dic['table']][dic['latitude']], table[dic['table']][dic['longitude']]]
    return {dic['table']: result}

def post(*args, **dic):
    return {}

def API(func):
    def wrapper(*args):
        func(*args)
    return wrapper
