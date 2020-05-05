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
## VS Code
* CTRL + SHIFT + P > Enable Linting
* CTRL + SHIFT + P > Run Linting
* CTRL + SHIFT + P > Select Linter