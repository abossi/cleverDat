#######
# manipulation of platform settings
#######

import os
import settings
from srcs.globals import *

#
# actualy, there are only 2 variables in the settings path of the platform:
# - TYPE: it's the type of the settings file (platform, project, plugin)
# - PROJECTS_PATHS: the list where the platform need to search projects
#

def get_projects_paths():
    """
    Parameters:

    No parameters.

    Effect:

    Return the list of projects path of the platform.
    """
    # if you need that I explain you that, that's mean you have nothing to do here! ;)
    return settings.PROJECTS_PATHS

def add_projects_paths(project_path):
    """
    Parameters:

    project_path: a new path of projects for the platform.

    Effect:

    Add the path to check projects and load them in the platform.
    """
    # don't add if already present in PROJECTS_PATHS
    if project_path in settings.PROJECTS_PATHS:
        return {
                "status": "error",
                "message": "this path is already a projects path",
        }
    # get the list of potentialy projects directories
    try:
        list_proj = os.listdir(project_path)
    except PermissionError:
        return {
                "status": "error",
                "message": "permission denied",
        }
    except FileNotFoundError:
        return {
                "status": "error",
                "message": "directory doesn't exist",
        }
    try:
        # add the path to the PROJECTS_PATHS in the settings file
        with open('settings.py', 'r') as f:
            lines = f.readlines()
        in_path = False
        with open('settings.py', 'w') as f:
            for line in lines:
                if line.startswith("PROJECTS_PATHS"):
                    in_path = True
                if in_path and line.startswith("]"):
                    in_path = False
                    f.write("        \"" + project_path + "\",\n")
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
    # add the path to the local PROJECTS_PATHS
    settings.PROJECTS_PATHS.append(project_path)
    # try to load all found projects
    for proj in list_proj:
        if os.path.isdir(os.path.join(project_path, proj)) and not proj.endswith("__"):
            proj = os.path.join(project_path, proj)
            load_proj(proj)
    return {
            "status": "success",
            "message": "path added...",
    }

def remove_projects_paths(project_path):
    """
    Parameters:

    project_path: the projects path to delete from the platform

    Effect:

    Remove the path in the platform and unload all projects corresponding from the platform.
    """
    # check if the path is in the list of PROJECTS_PATHS
    if not project_path in settings.PROJECTS_PATHS:
        return {
                "status": "error",
                "message": "this path is not in the projects paths list",
        }
    list_to_remove = []
    for i,el in enumerate(settings.PROJECTS_PATHS):
        if el == project_path:
            list_to_remove.append(i)
    for i in list_to_remove:
        del settings.PROJECTS_PATHS[i]
    # remove the line with the path in the settings file
    try:
        with open('settings.py', 'r') as f:
            lines = f.readlines()
        with open('settings.py', 'w') as f:
            in_path = False
            for line in lines:
                if line.startswith("PROJECTS_PATHS"):
                    in_path = True
                if in_path and line.startswith("]"):
                    in_path = False
                if not in_path or not line.startswith("        \"" + project_path + "\","):
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
    # remove all project from the platform
    list_to_remove = []
    for proj in projects.keys():
        if proj.rsplit('/', 1)[0] == project_path:
            list_to_remove.append(proj)
    for el in list_to_remove:
        del projects[el]
    return {
            "status": "success",
            "message": "path removed...",
    }

def get_list_widgets():
    return settings.PLATFORM_LIST_WIDGETS

def get_actu_widget():
    return settings.PLATFORM_ACTU_WIDGET
