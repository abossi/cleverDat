#######
# manipulation of projects
#######

import settings
from srcs.globals import *
import os
from shutil import copyfile, rmtree, move
import re

#
# all of this fonctions are here to manipulate projects
#          GET / CREATE / DELETE / EDIT
#
#
# physicaly, a project is a directory with a settings file who contain
# the TYPE 'project'.
#

def get_proj():
    """
    Parameters:

    No parameters.

    Effect:

    Return the list of projects loaded in the platform.
    """
    # did you realy need a comment?
    list_proj = {}
    for el in settings.PROJECTS_PATHS:
        list_proj[el] = []
    for el in list(projects.keys()):
        path_name = el.rsplit('/', 1)
        list_proj[path_name[0]].append(path_name[1])
    return list_proj

def create_proj(path, name):
    """
    Parameters:

    path: the path for the new project
    name: the name for the new project

    Effect:

    Create the project in the path and load it in the platform.
    Return a structure who valid or invalid the changement.
    """
    if not re.compile("^[a-zA-Z0-9_]+$").match(name):
        return {
                "status": "error",
                "message": "Not valide name: only alphanumeric and '_'."
        }
    proj = os.path.join(path, name)
    # create a directory with the with the name of the project
    try:
        os.mkdir(proj)
    except FileExistsError as e:
        return {
                "status": "error",
                "message": str(e),
        }
    except PermissionError:
        return {
                "status": "error",
                "message": "permission denied",
        }
    # add the settings file for the project
    with open("./patterns/project/settings.py") as f:
        lines = f.readlines()
    for i,line in enumerate(lines):
        if line == "PLUGINS_PATHS = [\n":
            lines.insert(i + 1, "        \"" + os.path.realpath("./plugins") + "\",\n")
    with open(os.path.join(proj, "settings.py"), 'w') as f:
        f.writelines(lines)
    # and load the project in the platform
    load_proj(proj)
    return {
            "status": "success",
            "message": "project created...",
    }

def delete_proj(path, name):
    """
    Parameters:

    path: the path of the project
    name: the name of the project

    Effect:

    Delete the project from the path and remove it from the platform.
    """
    # remove the directory of the project
    try:
        rmtree(os.path.join(path, name))
    except FileNotFoundError:
        return {
                "status": "error",
                "message": "project not found",
        }
    except PermissionError:
        return {
                "status": "error",
                "message": "permission denied",
        }
    # remove the project in the platform
    del projects[os.path.join(path, name)]
    return {
            "status": "success",
            "message": "project deleted...",
    }

def edit_proj(path, name, new_path, new_name):
    """
    Parameters:

    path: the path of the project
    name: the name of the project
    new_path: the new path for the project
    new_name: the new name for the project

    Effect:

    Change the path and the name of the project and reload it in the platform.
    Return a structure who valid or invalid the changement.
    """
    if not re.compile("^[a-zA-Z0-9_]+$").match(new_name):
        return {
                "status": "error",
                "message": "Not valide name: only alphanumeric and '_'."
        }
    # check if the name is not already used in the new path
    if new_name in os.listdir(new_path):
        return {
                "status": "error",
                "message": "project already exist",
        }
    # try to move all the project
    try:
        move(os.path.join(path, name), os.path.join(new_path, new_name))
    except FileNotFoundError:
        return {
                "status": "error",
                "message": "project not found",
        }
    except PermissionError:
        return {
                "status": "error",
                "message": "permission denied",
        }
    # del the old project from the platform and load the new one
    del projects[os.path.join(path, name)]
    load_proj(os.path.join(new_path, new_name))
    return {
            "status": "success",
            "message": "project edited...",
    }

def get_plugins_project(proj, func):
    result = []
    for el in projects[proj]['plugins'].keys():
        if func in projects[proj]['plugins'][el]['functions']:
            result.append(el)
    return result
