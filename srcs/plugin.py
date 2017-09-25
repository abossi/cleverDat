#######
# manipulation of plugins
#######

import os
from srcs.globals import *
from shutil import copyfile, move
import re
import sys

#
# utils
#

switch_parameters_to_string = {
    'bool' : lambda param: str(param),
    'str'  : lambda param: '\'' + param.replace('\'', '\\\'') + '\'',
    'int'  : lambda param: str(param),
    'float': lambda param: str(param)
}

def parameter_to_string(parameter):
    if parameter['type'] in switch_parameters_to_string.keys():
        return switch_parameters_to_string[parameter['type']](parameter['value'])
    return str(parameter['value'])

#
# all of this functions are here to manipulate plugin's scripts
#          GET / CREATE / DELETE / EDIT
#

def edit_id_plugins(lines, func):
    for i,line in enumerate(lines):
        if line.startswith("        def " + func):
            while lines[i - 1].startswith('        @'):
                i -= 1
            pos = 0
            while lines[i].startswith('        @'):
                lines[i] = re.sub('\([0-9]+, ', '(' + str(pos) + ', ', lines[i])
                i += 1
                pos += 1
            break
    return lines

def get_script_plugin(path, proj_name, script_name, functions):
    """
    Parameters:

    path: the path of the project
    proj_name: the name of the project
    script_name: the name of the script
    functions: the list of the functions to return decorators

    Effect:

    Return a dico where keys are functions parameters and values are the list list of decorators name in the order of call.
    """
    if script_name not in projects[os.path.join(path, proj_name)]['scripts'].keys():
        return {
                "status": "error",
                "message": "script not found"
        }
    result = {}
    # for all functions that you search plugins
    for func in functions:
        result[func] = []
        for el in projects[os.path.join(path, proj_name)]['scripts'][script_name]['plugins'][func]:
            result[func].append(el['name'])
    return result

def add_script_plugin(path, proj_name, script_name, plugin, function, position):
    """
    Parameters:

    path: the path of the project
    proj_name: the name of the project
    script_name: the name of the script
    plugin: the name of the plugin to add
    function: the function to add plugin
    position: the position in the plugin list

    Effect:

    Add the plugin to the function at the corresponding position.
    """
    # check if the plugin is compatible with this function
    if not function in projects[os.path.join(path, proj_name)]['plugins'][plugin]['functions']:
        return {
                "status": "error",
                "message": "plugin couldn't connect to this function"
        }
    # read the script
    try:
        with open(os.path.join(path, proj_name, script_name + ".py")) as f:
            lines = f.readlines()
    except FileNotFoundError:
        return {
                "status": "error",
                "message": "file not found",
        }
    except PermissionError:
        return {
                "status": "error",
                "message": "permission denied",
        }
    plugin_path = projects[os.path.join(path, proj_name)]['plugins'][plugin]['path']
    # get the good index of the PLUGINS_PATHS and add the dynamique load in the script
    for i,el in enumerate(projects[os.path.join(path, proj_name)]['settings']['PLUGINS_PATHS']):
        if os.path.join(path, proj_name, el) == plugin_path:
            line_to_write = plugin + " = SourceFileLoader(\"plugins." + plugin + "\", settings.PLUGINS_PATHS[" + str(i) + "] + \"/" + plugin + "/" + plugin + ".py\").load_module()\n"
            break
    else:
        return {
                "status": "error",
                "message": "plugin unknown",
        }
    for i,line in enumerate(lines):
        if line == "import settings\n":
            lines.insert(i + 2, line_to_write)
            break
    else:
        return {
                "status": "error",
                "message": "fail script parsing, import settings not found",
        }
    # build list of parameters for decoration
    param_list = projects[os.path.join(path, proj_name)]['plugins'][plugin]['parameters']
    str_param = ''
    first_param = True
    for key in param_list.keys():
        if not first_param:
            str_param += ', '
        str_param += key + ' = ' + parameter_to_string(param_list[key])
        first_param = False
    # insert the decoration at the good position
    position = int(position)
    for i,line in enumerate(lines):
        if line.startswith("        def " + function):
            if position < 0 or i - position < 0 or (position != 0 and not lines[i - position].startswith("        @")):
                return {
                        "status": "error",
                        "message": "wrong position",
                }
            lines.insert(i - position, "        @" + plugin + ".plugin(" + str(position) + ', ' + str_param + ")\n")
            lines = edit_id_plugins(lines, function)
            break
    else:
        return {
                "status": "error",
                "message": "function not found",
        }
    # write the new file
    try:
        with open(os.path.join(path, proj_name, script_name +".py"), "w") as f:
            f.writelines(lines)
    except PermissionError:
        return {
                "status": "error",
                "message": "permission denied",
        }
    # reload the singleton
    load_script(os.path.join(path, proj_name), script_name + ".py")
    return {
            "status": "success",
            "message": "plugin added",
    }

def remove_script_plugin(path, proj_name, script_name, plugin, function, position):
    """
    Parameters:

    path: the path of the project
    proj_name: the name of the project
    script_name: the name of the script
    plugin: the name of the plugin to add
    function: the function to add plugin
    position: the position in the plugin list

    Effect:

    Remove the plugin to the function at the corresponding position.
    """
    # check if the plugin is compatible with this function
    if not function in projects[os.path.join(path, proj_name)]['plugins'][plugin]['functions']:
        return {
                "status": "error",
                "message": "plugin couldn't connect to this function"
        }
    # read the script
    try:
        with open(os.path.join(path, proj_name, script_name + ".py")) as f:
            lines = f.readlines()
    except FileNotFoundError:
        return {
                "status": "error",
                "message": "file not found",
        }
    except PermissionError:
        return {
                "status": "error",
                "message": "permission denied",
        }
    # found the plugin and remove it
    for i,line in enumerate(lines):
        if line.startswith("        def " + function):
            while lines[i - 1].startswith("        @"):
                i -= 1;
            if not lines[i + position].startswith("        @" + plugin):
                return {
                        "status": "error",
                        "message": "wrong position or plugin",
                }
            del lines[i + position]
            break
    else:
        return {
                "status": "error",
                "message": "function not found",
        }
    lines = edit_id_plugins(lines, function)
    # found the dynamique import and remove it
    for i,line in enumerate(lines):
        if line.startswith(plugin + " = SourceFileLoader(\"plugins." + plugin):
            del lines[i]
            break
    else:
        return {
                "status": "error",
                "message": "plugin unknown",
        }
    # write the script
    try:
        with open(os.path.join(path, proj_name, script_name +".py"), "w") as f:
            f.writelines(lines)
    except PermissionError:
        return {
                "status": "error",
                "message": "permission denied",
        }
    # reload the script
    load_script(os.path.join(path, proj_name), script_name + ".py")
    return {
            "status": "success",
            "message": "plugin deleted",
    }

def get_script_plugin_param(path, proj_name, script_name, function, position):
    return projects[os.path.join(path, proj_name)]['scripts'][script_name]['plugins'][function][int(position)]['parameters']

def set_script_plugin_param(path, proj_name, script_name, function, position, parameters):
    plugin_name = projects[os.path.join(path, proj_name)]['scripts'][script_name]['plugins'][function][int(position)]['name']
    for param in projects[os.path.join(path, proj_name)]['plugins'][plugin_name]['parameters'].keys():
        if not param in parameters.keys():
            print(parameters)
            return {
                    "status": "error",
                    "message": "not every parameters",
            }

    # read the script
    try:
        with open(os.path.join(path, proj_name, script_name + ".py")) as f:
            lines = f.readlines()
    except FileNotFoundError:
        return {
                "status": "error",
                "message": "file not found",
        }
    except PermissionError:
        return {
                "status": "error",
                "message": "permission denied",
        }
    # build list of parameters for decoration
    str_param = ''
    first_param = True
    for key in parameters.keys():
        if not first_param:
            str_param += ', '
        str_param += key + ' = ' + parameter_to_string({
            'type': type(parameters[key]).__name__,
            'value': parameters[key]
            })
        first_param = False
    # insert the decoration at the good position
    position = int(position)
    for i,line in enumerate(lines):
        if line.startswith("        def " + function):
            if position < 0 or i - position < 0 or (position != 0 and not lines[i - position].startswith("        @")):
                return {
                        "status": "error",
                        "message": "wrong position",
                }
            i -= 1;
            while lines[i].startswith("        @"):
                i -= 1;
            lines[i + position + 1] = "        @" + plugin_name + ".plugin(" + str(position) + ', ' + str_param + ")\n"
            break
    else:
        return {
                "status": "error",
                "message": "function not found",
        }
    # write the new file
    try:
        with open(os.path.join(path, proj_name, script_name +".py"), "w") as f:
            f.writelines(lines)
    except PermissionError:
        return {
                "status": "error",
                "message": "permission denied",
        }
    # reload the singleton
    load_script(os.path.join(path, proj_name), script_name + ".py")
    return {
            "status": "success",
            "message": "parameters edited...",
    }
