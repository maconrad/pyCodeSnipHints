Libraries
========

## Python Standard Library
* Instead of ex

| Library | function / Class etc. | Description |
|-----------|---------------------|----------------|
|string  |{0:d} / {:^30}   |Format, align etc.  |
|functools  |reduce, wraps, total_ordering, cache, singledispatch |N to 1 mapping, decorators, caching, method overloading  |
|itertools  |groupby, iter, next, compress, count, cycle, repeat, starmap, combination, permutation, product, islice, accumulate, filterfalse, tee | iterator tools |
|futures    |annotations          |     |
|re         |          |Regex           |
|datetime   |          |                |
|collections|          |                |
|types      |          |                |
|pprint     |          |                |
|numbers    |          |                |
|math       |          |                |
|random    |          |                |
|pathlib    |          |                |
|pickle    |          |                |
|csv    |          |                |
|configparser    |          |                |
|os    |          |                |
|io    |          |                |
|distutils|||
|sys    |argv, exit, flags, windowsversion, path, platform, ps1/ps2, stdout/stdin/stderr/, version, etc. |System Information, functions, params|
|time    |          |                |
|argparse    |          |                |
|logging    |          |                |
|errno    |          |                |
|formatter    |          |                |
|abc    |metaclass |Abstract Base Classes |
|contextlib|@contextmanager|with-Statement|
|dataclasses|@dataclass|Annotate instance vars, __init__(), __repr__() and other methods such as __lt__() are auto-generated, PEP557|
|timeit|||
|test|||
|unittest|setUp(), tearDown(), @skipIf, python -m unittest discover|Built-in Unit Testing Library|
|doctest|||
|pydoc|||
|typing|||
|gettext||i10n|
|locale||i10n|
|ipaddress|||
|xmlrpc||Server and Client|
|http||Server, Cookie, Cookiejar|
|uuid||UUID Processing|
|urllib||URL Handling|
|xml||Parser, DOM, etree, SAX|
|html||Parsers, definitions|
|json||Json|
|email||MIME Email|
|base64|||
|binhex||Convert|
|binascii||Convert|
|ssl|||
|socket|||
|asyncio|||

* Threading

| Library | function / Class etc. | Description |
|-----------|---------------------|----------------|
|threading    |          |                |
|multiprocessing    |          |                |
|concurrent    |          |                |
|queue    |          |                |
|sched    |          |                |

* Windows

| Library | function / Class etc. | Description |
|-----------|---------------------|----------------|
|msilib  |     |Microsoft Installer Files  |
|winreg  |      |Windows Registry Access  |


## PyPi
* Building / Linting / Testing


| Library | function / Class etc. | Description |
|-----------|---------------------|----------------|
|tox        |tox.ini, tox-quickstart, tox -e py38, tox -e py38 -- tests -k unit|Automation, Build, Test and Release Workflow / Testing in different python versions ("replacement for make that is python specific") / command runner|
|pytest     |python -m pytest -vv --durations=3 -m dummymarking , @pytest.fixture, @pytest.mark.name, @pytest.mark.parametrize (+skip, skipif, parametrization), monkeypatch|No need to inherit from a base class as with unittest, compatible with unittest, marking tests, durations, plugins like pytest-django, pytest-randomly, pytest-cov|
|nose, nose2||Alternative to pytest|
|pytest-randomly|pytest -p no:randomly, pytest --randomly-seed=123|When installed pytest runs tests randomly automatically, rerun with same random seed|
|flake8     |.flake8 or setup.cfg|Enable or disable warnings|
|isort      |       |Reorder import satements to PEP recommended order|
|mccabe     |        |Code complexity checker|
|mypy       |e.g. from typing import Union, Any, Type, SupportsFloat, Dict|Static code analyser based on type hints, integrated into VS Code|
|pre-commit |       |                |
|pylint     |         |                |
|virtualenv |         |                |
|virtualenvwrapper     |          |        |
|virtualenv |       |                |
|monkeytype|run, stub, apply|Find types used at runtime to move to typed system. Annotate legacy code|
|pyre||Alternative to mypy for large code base|
|typing_extensions|Protocol|Structural typing - program to an interface|

* Web


| Library | function / Class etc. | Description |
|-----------|---------------------|----------------|
|Request    |                |                |
|Django    |                     |                |
|Flask    |      |                |
|BeautifulSoup    |      |
|Selenium  |
|    |      |

* Data Science


| Library | function / Class etc. | Description |
|-----------|---------------------|----------------|
|Numpy    |                     |                |
|Pandas|||
|Matplotlib|||
|Opencv|||
||||

* Machine Learning

| Library | function / Class etc. | Description |
|-----------|---------------------|----------------|
|Tensorflow    |   |                |
|Keras|||
|PyTorch|||
|Sci-kit Learn|||
||||

* GUI

| Library | function / Class etc. | Description |
|-----------|---------------------|----------------|
|PyQt5    |   |                |
|Tkinter|||
||||

* Diverses

| Library | function / Class etc. | Description |
|-----------|---------------------|----------------|
|    |    |                |
|sdf    |                     |                |
|xy     |                     |                |
