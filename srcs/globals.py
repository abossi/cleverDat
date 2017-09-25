# WARNING: you are in the deeper file of the project!
# all scripts call this one to have access to the projects variable
#
#                  IMPORT                         IMPORT
#               +-------------> project.py ---------------+
#               +-------------> script.py ----------------+
#    platform.py+-----------------------------------------+---> globals.py
#               +--------> settings_platform.py ----------+
#               +--------> settings_project.py -----------+
#
#
# there are also intern functions that is depreciate to call it

import os
from importlib.machinery import SourceFileLoader
import re

# THE projects variable!
#
# it's look like:
#
# {
#   'path1/project1': {
#     'settings': {
#       'PLUGINS_PATHS': ['path1', 'path2']
#     },
#     'scripts': {
#       'script1': <the singleton of the script1>,
#       'script2': <the singleton of the script2>
#     },
#     'plugins': {
#       'plugins1': {
#         'path': 'path/plugin1',
#         'functions': ['imp', 'proc', 'exp'],
#         'plugin': <the plugin's decorator>,
#         'API': <the API's decorator>
#       },
#       'plugins2': {
#         'path': 'path/plugin2',
#         'functions': ['imp', 'proc', 'exp'],
#         'plugin': <the plugin's decorator>,
#         'API': <the API's decorator>
#       }
#     }
#   },
#   'path1/project2': {
#     ...
#   }
#   'path2/project1': {
#     ...
#   }
#   ...
# }
#
projects = {}

#
# utils
#

switch_string_to_parameter = {
    'str': lambda param: param.replace('\\\'', '\'')[1:-1],
    'int': lambda param: int(param),
    'bool': lambda param: bool(param),
    'float': lambda param: float(param)
}

def string_to_parameter(string, parameter_type):
    if parameter_type in switch_string_to_parameter.keys():
        return switch_string_to_parameter[parameter_type](string)
    return string

def load_script(proj, script):
    """
    Parameters:

    proj: name of the project
    script: name of the cript

    Effect:

    Load the script in the projects structure to have acces to the singleton like:
    projects[proj]['scripts'][script]

    Warrning:

    Don't use this fonction if you don't know what you do.
    Use create_script and edit_script who know! ;)
    """
    # need the .py in the script variable
    project_name = "{}/{}".format(proj, script)
    try:
        module = SourceFileLoader(script.replace(".py", ""), project_name).load_module()
    except ValueError:
        pass
    except NameError:
        pass
    except PermissionError:
        pass
    else:
        try:
            with open(project_name) as f:
                lines = f.readlines()
        except FileNotFoundError:
            return
        except PermissionError:
            return
        result = {}
        # for all functions that you search plugins
        for func in ['imp', 'proc', 'exp']:
            result[func] = []
            i = 0
            # you search the function definition
            while i < len(lines) and not lines[i].startswith("        def " + func):
                i += 1
            if i != len(lines):
                i -= 1
                # and you get all decorations on it
                while lines[i].startswith("        @") and i >= 0:
                    plugin = {}
                    plugin['name'] = re.search('@([a-zA-Z_]+)\.', lines[i]).group(1)
                    plugin['parameters'] = {}
                    parameters = re.search('\((.+)\)', lines[i]).group(1).split(', ')
                    for param in projects[proj]['plugins'][plugin['name']]['parameters'].keys():
                        for para in parameters:
                            if para.startswith(param):
                                plugin['parameters'][param] = string_to_parameter(re.search(' = (.+)', para).group(1), projects[proj]['plugins'][plugin['name']]['parameters'][param]['type'])
                    result[func].insert(0, plugin)
                    i -= 1
        # if we have load the script without problem, we add the singleton to the projects variable
        # ... if there are a singleton ...
        try:
            projects[proj]["scripts"][script.replace(".py", "")] = {
                    'sing': module.singleton,
                    'plugins': result,
            }
        except AttributeError:
            pass

def load_plugin(proj, plugin_path, plugin):
    """
    Parameters:

    proj: name of the project
    plugin_path: path of the plugin
    plugin: name of the plugin

    Effect:

    Load the plugin in the projects structure to have acces to decorations functions like:
    projects[proj]["plugins"][plugin].plugin(lambda x : x)
    projects[proj]["plugins"][plugin].API(lambda x : x)

    Warning:

    Don't use this function if you don't know what you do.
    """
    plugin_name = "{}/{}/{}.py".format(plugin_path, plugin, plugin)
    # try to load the plugin
    try:
        module = SourceFileLoader(plugin, plugin_name).load_module()
    except:
        pass
    else:
        try:
            with open(plugin_name) as f:
                plugin_lines = f.readlines()
        except FileNotFoundError:
            return
        except PermissionError:
            return
        # we add the plugin if there are a func, a plugin and an API...
        try:
            projects[proj]["plugins"][plugin] = {
                    "path": plugin_path,
                    "functions": module.func,
                    "plugin": module.plugin,
                    "API": module.API,
                    'parameters': module.parameters
            }
        except AttributeError:
            pass

def load_proj(proj):
    """
    Parameters:

    proj: name of the project

    Effect:

    Load the project in the projects structure to have acces to it like:
    projects[proj]

    Warrning:

    Don't use this function if you don't know what you do.
    Use create_proj and edit_proj who know! ;)
    """
    # we get all inside the proj directory
    try:
        list_script = os.listdir(proj)
    except PermissionError:
        return
    # we try to load the settings file
    try:
        proj_settings = SourceFileLoader("settings",
                os.path.join(proj, "settings.py")).load_module()
    except FileNotFoundError:
        return
    except PermissionError:
        return
    # we check if it's a project settings (if it's a platform setting, we fall in an infiny loop)
    if proj_settings.TYPE != "project":
        return
    # we are sure that it's a project, we add it
    projects[proj] = {
            "scripts": {},
            "plugins": {},
            "settings": {},
    }
    # we load all plugins
    for plugin_path in proj_settings.PLUGINS_PATHS:
        plugin_path = os.path.join(proj, plugin_path)
        for plugin in os.listdir(plugin_path):
            load_plugin(proj, plugin_path, plugin)
    # we load all scripts
    projects[proj]["settings"]["PLUGINS_PATHS"] = proj_settings.PLUGINS_PATHS
    projects[proj]["settings"]["LIST_WIDGETS"] = proj_settings.LIST_WIDGETS
    projects[proj]["settings"]["ACTU_WIDGET"] = proj_settings.ACTU_WIDGET
    for script in list_script:
        if script.endswith(".py"):
            load_script(proj, script)
