
################################################
# func variable set in witch function
# your plugin could be connected:
#
# possible values:
# 'imp' and/or 'proc' and/or 'exp'
#
# need to be a list!
################################################
func = ["proc"]

################################################
# parameters variable give all parameters
# needed for your decorator:
#
# it's a dictionary.
# keys are names of parameters
# and contain 'value' who is the default
# parameter and 'type'.
# 'type' is actualy not used.
# 
# In this exemple:
# @cd_hello_world.plugin(0, value = 'Hello world!')
#
################################################
parameters = {
    'text': {
        'value': "Hello world!",
        'type': 'str'
    }
}

################################################
# your decorator!
#
# If you need to touch it, don't tuch it!
#
# If you REALY need to touch it, REALY don't
# touch it!
################################################
def plugin(id, **dic):
    def decorator(func):
        def wrapper(*args):
            tmp = pre(**dic)
            data = func(*args)
            # but you can set tmp with post return like that:
            # tmp = post(**dic)
            post(**dic)
            if args[1] == -1 or args[1] < id:
                data.insert(0, tmp)
                return data
            elif args[1] == id:
                return tmp
            return data
        return wrapper
    return decorator

################################################
# This is the pre function of your decorator.
#
# All of this code is execute before the call
# of the function.
#
# The return is the structure who is return
# to your widget.
#
# Actualy only tested with dictionary.
################################################
def pre(**dic):
    print("a log for user ;)")
    return {'text': dic['text']}

################################################
# This is th post function of your decorator.
#
# All of this code is execute after the call
# of the function.
#
# The return could be the returned structure
# if you modify THE AUTORISED line in
# your decorator.
#
# Actualy only tested with dictionary.
################################################
def post(**dic):
    return {}

################################################
# history function. Not used. Could be remove
# in the future.
################################################
def API(func):
    def wrapper(*args):
        func(*args)
    return wrapper
