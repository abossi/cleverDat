#######
# manipulation of scripts
#######

import os
from srcs.globals import *
from shutil import copyfile, move
import re
import sys

#
# all of this functions are here to manipulate scripts
#          GET / CREATE / DELETE / EDIT
#

def get_script(path, proj_name):
    """
    Parameters:

    path: the path of the project
    proj_name: the name of the project

    Effect:

    Return the list of scripts loaded in the project platform.
    """
    # just get scripts...
    proj = os.path.join(path, proj_name)
    return list(projects[proj]["scripts"].keys())

def create_script(path, proj_name, script_name):
    """
    Parameters:

    path: the path of the project
    proj_name: the name of the project
    script_name: the name for the project

    Effect:

    Create the script in the project and load it in the platform.
    Return a structure who valid or invalid the changement.
    """
    if not re.compile("^[a-zA-Z0-9_]+$").match(script_name):
        return {
                "status": "error",
                "message": "Not valide name: only alphanumeric and '_'."
        }
    proj = os.path.join(path, proj_name)
    # check if the name is not already used
    if script_name + ".py" in os.listdir(proj):
        return {
                "status": "error",
                "message": "script already exist",
        }
    # copy the script pattern with the good name
    try:
        copyfile("./patterns/project/script.py", os.path.join(proj, script_name + ".py"))
    except PermissionError:
        return {
                "status": "error",
                "message": "permission denied",
        }
    # load the script
    load_script(proj, script_name + ".py")
    return {
            "status": "success",
            "message": "script created...",
    }

def delete_script(path, proj_name, script_name):
    """
    Parameters:

    path: the path of the project
    proj_name: the name of the project
    script_name: the name of the script

    Effect:

    Delete the script from the project and remove it from the platform.
    """
    # remove the file
    try:
        os.remove(os.path.join(path, proj_name, script_name + ".py"))
    except FileNotFoundError:
        return {
                "status": "error",
                "message": "script not found",
        }
    except PermissionError:
        return {
                "status": "error",
                "message": "permission denied",
        }
    # del the script in the platform
    del projects[os.path.join(path, proj_name)]['scripts'][script_name]
    return {
            "status": "success",
            "message": "script deleted...",
    }

def edit_script(path, proj_name, script_name, new_script_name):
    """
    Parameters:

    path: the path of the project
    proj_name: the name of the project
    script_name: the name of the script
    new_script_name: the new name for the script

    Effect:

    Change the name of the script and reload it in the platform.
    Return a structure who valid or invalid the changement.
    """
    if not re.compile("^[a-zA-Z0-9_]+$").match(new_script_name):
        return {
                "status": "error",
                "message": "Not valide name: only alphanumeric and '_'."
        }
    # check if the new name is already used
    if new_script_name + ".py" in os.listdir(os.path.join(path, proj_name)):
        return {
                "status": "error",
                "message": "script already exist",
        }
    # move the script
    try:
        move(os.path.join(path, proj_name, script_name + ".py"),
                os.path.join(path, proj_name, new_script_name + ".py"))
    except FileNotFoundError:
        return {
                "status": "error",
                "message": "script not found",
        }
    except PermissionError:
        return {
                "status": "error",
                "message": "permission denied",
        }
    # edit the script in the platform
    del projects[os.path.join(path, proj_name)]['scripts'][script_name]
    load_script(os.path.join(path, proj_name), new_script_name + ".py")
    return {
            "status": "success",
            "message": "script edited...",
    }

def get_content_function(path, proj_name, script_name, function):
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
    result = ""
    inside = False
    for line in lines:
        if line == '\n':
            inside = False
        if inside:
            result += line[12:]
        if line.startswith("        def " + function + "(self"):
            inside = True
    return {
            "status": "success",
            "message": result,
    }

def set_content_function(path, proj_name, script_name, function, content):
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
    newlines = []
    inside = False
    for line in lines:
        if line == '\n':
            inside = False
        if not inside:
            newlines.append(line)
        if line.startswith("        def " + function + "(self"):
            newlines.append(content)
            inside = True
    # write the script
    try:
        with open(os.path.join(path, proj_name, script_name +".py"), "w") as f:
            f.writelines(newlines)
    except PermissionError:
        return {
                "status": "error",
                "message": "permission denied",
        }
    load_proj(os.path.join(path, proj_name))
    return {
            "status": "success",
            "message": "function edited...",
    }

def run_script(path, proj_name, script_name, function):
    result = {}
    ORIGIN_PATH = os.getcwd()
    os.chdir(os.path.join(path, proj_name))
    try:
        result = projects[path + '/' + proj_name]['scripts'][script_name]['sing'].run(function)
        result['status'] = 'success'
    except Exception as e:
        sys.stdout = sys.__stdout__
        result['error'] = str(e)
        result['status'] = 'danger'
    result['script'] = script_name
    os.chdir(ORIGIN_PATH)
    return result

def run_script_return(path, proj_name, script_name, function, api, pos):
    result = {}
    ORIGIN_PATH = os.getcwd()
    os.chdir(os.path.join(path, proj_name))
    try:
        result = projects[path + '/' + proj_name]['scripts'][script_name]['sing'].run(function, api = api, pos = pos)
    except Exception as e:
        sys.stdout = sys.__stdout__
        result['error'] = str(e)
        result['status'] = 'danger'
    os.chdir(ORIGIN_PATH)
    return result
