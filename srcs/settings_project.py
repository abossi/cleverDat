#######
# manipulation of platform settings
#######

import os
import settings
from srcs.globals import *
from importlib.machinery import SourceFileLoader

#
# actualy, there are only 2 variables in the settings path of the project:
# - TYPE: it's the type of the settings file (platform, project, plugin)
# - PLUGINS_PATHS: the list where the project need to search plugins
#

def get_plugins_paths(proj):
    """
    Parameters:

    proj: the project to check plugins

    Effect:

    Return the list of plugins path of the project.
    """
    # load the settings file of the project
    try:
        proj_settings = SourceFileLoader("settings",
                os.path.join(proj, "settings.py")).load_module()
    except FileNotFoundError:
        return {
                "status": "error",
                "message": "File not found",
        }
    except PermissionError:
        return {
                "status": "error",
                "message": "permission denied",
        }
    # return the PLUGINS_PATHS list
    return proj_settings.PLUGINS_PATHS

def add_plugins_paths(proj, plugin_path):
    """
    Parameters:

    proj: the project to add plugins.
    plugin_path: a new path of plugins for the project.

    Effect:

    Add the path to check plugins and load them in the project.
    """
    # get the list of potentialy projects directories
    # could be relatif or absolute
    try:
        if plugin_path.startswith('/'):
            list_plugins = os.listdir(plugin_path)
        else:
            list_plugins = os.listdir(os.path.join(proj, plugin_path))
    except PermissionError:
        return {
                "status": "error",
                "message": "permission denied",
        }
    if plugin_path in projects[proj]['settings']['PLUGINS_PATHS']:
        return {
                "status": "error",
                "message": "Path already exist!",
        }
    try:
        # add the path to the PLUGINS_PATHS in the settings file
        with open(os.path.join(proj, 'settings.py'), 'r') as f:
            lines = f.readlines()
        in_path = False
        with open(os.path.join(proj, 'settings.py'), 'w') as f:
            for line in lines:
                if line.startswith("PLUGINS_PATHS"):
                    in_path = True
                if in_path and line.startswith("]"):
                    f.write("        \"" + plugin_path + "\",\n")
                f.write(line)
    except FileNotFoundError:
        return {
                "status": "error",
                "message": "'settings.py' not found",
        }
    except PermissionError:
        return {
                "status": "error",
                "message": "permission denied",
        }
    # reload the project, the effect is that you reload the plugins to
    load_proj(proj)
    return {
            "status": "success",
            "message": "path added...",
    }

def remove_plugins_paths(proj, plugin_path):
    """
    Parameters:

    proj: the project to remove plugins
    plugin_path: the plugins path to delete from the project

    Effect:

    Remove the path in the project and unload all plugins corresponding from the project.
    """
    # remove the line with the path in the settings file
    try:
        with open(os.path.join(proj, 'settings.py'), 'r') as f:
            lines = f.readlines()
        with open(os.path.join(proj, 'settings.py'), 'w') as f:
            for line in lines:
                if not line.startswith("        \"" + plugin_path + "\","):
                    f.write(line)
    except FileNotFoundError:
        return {
                "status": "error",
                "message": "'settings.py' not found",
        }
    except PermissionError:
        return {
                "status": "error",
                "message": "permission denied",
        }
    # remove all plugins from the project
    list_to_remove = []
    for plugin in projects[proj]['plugins'].keys():
        if projects[proj]['plugins'][plugin]['path'].endswith(plugin_path):
            list_to_remove.append(plugin)
    for el in list_to_remove:
        del projects[proj]['plugins'][el]
    return {
            "status": "success",
            "message": "plugin path removed...",
    }

def get_project_list_widgets(proj):
    return projects[proj]['settings']['LIST_WIDGETS']

def get_project_actu_widget(proj):
    return projects[proj]['settings']['ACTU_WIDGET']
