# Synopsis

DataView is a data visualization staging for import/edit/export data as REST API. All is plugin with a custom dashboard. Enjoy!

# Installation

You can directly clone the project from gitlab:

```
git clone git@gitlab.com:abossi/DataView.git
cd DataView
```

# Start

To generate projects structure:

```
python3.6
import platform
```

To create a new project and add a new script:

```
platform.create_proj("./projects", "my_badas_project")
platform.create_script("./projects", "my_badas_project", "script_who_make_coffee")
```

Or you can use the API:

```
python3.6 platform.py
```

And launch the url http://127.0.0.1:5000

# TODO list

- [x] create the project
- [x] build plugins and projects structures
- [ ] build API structure with Django
- [ ] create standard API for create/edit/delete project/script/plugin
- [ ] create basic dashboard for the PoC

# Contributors

Actualy main contributors are:
- [Maxime Meissonnier](https://gitlab.com/uusername)
- [Adrien Bossi](https://gitlab.com/abossi)

# Pull request

To check that your code follows pep8's rules, execute it at the projet's root:

```
brew install flake8
flake8
```

# Contact us

Every wednesday afternoon, we make a meeting at 42 school. Everybody are welcome to come/participate. If you are not student, contact one of us to get an autorisation.

# License

License MIT.
