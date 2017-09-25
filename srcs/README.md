# Synopsis

This directory is the location of all platform functions. We have make this for clarity reasons.

### settings_platform.py

This file have all functions for settings platform manipulation:
 - GET the list of projects path
 - ADD e project path
 - REMOVE a project path

### project.py

This file have all functions for projects manipulation:
 - GET the list of all projects
 - CREATE a new project in designed path
 - DELETE an existing project from designed path
 - EDIT the name and the path of the project

### settings_projects.py

This file have all functions for settings projects manipulation:
 - GET the list of plugins path
 - ADD a plugin path
 - REMOVE a plugin path

### script.py

This file have all functions for script manipulation:
 - GET the list of script for one project
 - CREATE a new script in designed project
 - DELETE an existing script from designed project
 - EDIT the name of the script from a designed project
 - GET the plugins list for designed functions of a script
 - ADD a plugin for designed function's script
 - REMOVE a plugin from designed function's script

### globals.py

This is the deeper file of the project!
all scripts call this one to have access to the projects variable

```
               IMPORT                         IMPORT
            +-------------> project.py ---------------+
            +-------------> script.py ----------------+
 platform.py+-----------------------------------------+---> globals.py
            +--------> settings_platform.py ----------+
            +--------> settings_project.py -----------+
```

There are also intern functions that is depreciate to call it:
 - LOAD a script
 - LOAD a plugin
 - LOAD a project
