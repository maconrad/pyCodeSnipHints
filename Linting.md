Formating and Linting
======

## PEP8
* spaces, not tabs
* <span style="color:green">variable_name</span>, not <span style="color:red">variableName</span> or <span style="color:red">VariableName</span>
* No extra whitespaces
{'good': 42}
{'bad' : 20}
***

## Linting Tools
* pylint
* flake8
* mypy
* mccabe
* isort
* autopep8
***

## Type Hints & Docstrings
* Type Hints for weakly typed languages like JS/Python -> Help Editor
* Docstring See also [PEP484 Type Hints](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
* See also [Microsoft4Developers](https://www.youtube.com/watch?v=P1B0ytn6VPU&list=PLlrxD0HtieHiXd-nEby-TMCoUNwhbLUnj&index=2)

```python
def print_hello(name: str) -> str:
	"""
	Greets user by name

	Parameters:
		name (str): Name of the user
	Returns:
		str: greeting
	"""
	print('hello, ' + name)
```
***

## Flake8 Settings
```shell
[flake8]
exclude = .git,__pycache__,docs,old,build,dist
max-complexity = 30
max-line-length=120
# E261: at least two spaces before inline comment
# E266: too many leading ‘#’ for block comment
# W504: line break after binary operator
# E302: Expected 2 Blank Lines, Found one
# E302: Expected 2 Blank Lines after class or function, Found one
# E402: module level import not at top of file
# F403, F05: wildcard import issue
# E722: bare except
# F401: Imported but unused
# E741: ambiguous variable name
ignore=E261,E266,E302,E305,W504,E402,F403,F405,E722,F401,E741
```

## VS Code
* CTRL + SHIFT + P > Enable Linting
* CTRL + SHIFT + P > Run Linting
* CTRL + SHIFT + P > Select Linter
* Plugins
	*
