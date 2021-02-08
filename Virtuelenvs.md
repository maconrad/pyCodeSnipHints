# Virtualenvs

## Overview
* conda (dependency mgmt)
* virtualenvwrapper
* pipenv (lock file)

## Virtualenvwrapper
* Environment Vars
  * $WORKON_HOME -- location where vEnvs are stored
  * $VIRTUAL_ENV -- Location of currently active vEnv


| virtualenvwrapper command                               | Description                          |
|---------------------------------------------------------|--------------------------------------|
| mkvirtualenv <name>                                     | Create new virtualenv                |
| lsvirtualenv                                            | List all virtualenvs                 |
| workon <name>                                           | Switch to a particular venv          |
| deactivate                                              | Deactivate a particual venv          |
| workon <name>                                           | Switch to a particular venv          |
| rmvirtualenv <name>                                     | Remove a venv                        |
| lssitepacketes \| cdsitepackages                        | List Site packages and jump to folder|
| allvirtualenv pip install -U pip                        | Update pip in all virtual envs       |

## Links
- [Compare Tools](https://stackoverflow.com/questions/38217545/what-is-the-difference-between-pyenv-virtualenv-anaconda)
- [Virtualenvwrapper setup](https://swapps.com/blog/how-to-configure-virtualenvwrapper-with-python3-in-osx-mojave/)