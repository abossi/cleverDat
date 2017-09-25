"""
0.0.1

SETTINGS PLATFORM:

def get_projects_paths()
def add_projects_paths(project_path)
def remove_projects_paths(project_path)


SETTINGS PROJECT:

def get_plugins_paths(proj)
def add_plugins_paths(proj, plugin_path)
def remove_plugins_paths(proj, plugin_path)


PROJECT:

def get_proj()
def create_proj(path, name)
def delete_proj(path, name)
def edit_proj(path, name, new_path, new_name)


SCRIPT:

def get_script(path, proj_name)
def create_script(path, proj_name, script_name)
def delete_script(path, proj_name, script_name)
def edit_script(path, proj_name, script_name, new_script_name)

def get_script_plugin(path, proj_name, script_name, functions)
def add_script_plugin(path, proj_name, script_name, plugin, function, position)
def remove_script_plugin(path, proj_name, script_name, plugin, function, position)

"""
import os

try:
    os.chdir(os.path.dirname(__file__))
except FileNotFoundError:
    pass

# import settings of the plqtform and all access fonctions in srcs directory
# just go to learn what there are inside ;)
import settings
from srcs.globals import *
from srcs.project import *
from srcs.script import *
from srcs.plugin import *
from srcs.settings_platform import *
from srcs.settings_project import *

from api.app import app
import api.project
import api.settings_platform
import api.settings_project
import api.script
import api.plugin

# load all projects from PROJECTS_PATHS in settings
# considerate a project if it's a directory who don't start with '__'...
# it could be better!
new_list_path = []
for proj_path in settings.PROJECTS_PATHS:
	try:
	    for proj in os.listdir(proj_path):
	        if os.path.isdir(proj_path + "/" + proj) and not proj.endswith("__"):
	            proj = os.path.join(proj_path, proj)
	            load_proj(proj)
	    new_list_path.append(proj_path)
	except FileNotFoundError:
		pass
	except PermissionError:
		pass
settings.PROJECTS_PATHS = new_list_path

# just print the project structure because it's beautiful!
print("\nprojects:")
print(projects)

if __name__ == '__main__':
    app.run()
