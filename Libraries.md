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
|collections|Counter, defaultDict, deque, ChainMap |Enhances dict,list,tuple functionality for special use Cases|
|copy|copy.copy(), copy.deepcopy()|Deep and Shallow copying|
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
|dataclasses-json|@dataclass_json| Annotate to easily encode/decode into/from json, 3rd party lib|
|timeit|||
|test|||
|unittest|setUp(), tearDown(), @patch, @skipIf, python -m unittest discover|Built-in Unit Testing Library to unittest.mock for Mocking|
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
|winrm or pywinrm   |      | Windows access via VMI, Powershell, cmd, for Kereberos see documentatoin on pypi |

## PyPi
* Building / Linting / Testing
* Mocking
  * Flask
  * Falcon + Gunicorn
  * Prism API Server (based on Openapi document)
  * Stoplight (hosted mock api server)
  * Postman (Easy mocking if access to real api -> save examples)


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
|pre-commit |pre-commit install, pre-commit run --all-files |Git Hooks before committing, e.g. flake8, mypy, trailing whitespaces etc.|
|pylint     |         |                |
|virtualenv |         |                |
|virtualenvwrapper     |          |        |
|virtualenv |       |                |
|monkeytype|run, stub, apply|Find types used at runtime to move to typed system. Annotate legacy code|
|pyre||Alternative to mypy for large code base|
|typing_extensions|Protocol|Structural typing - program to an interface|
|tqdm|tqdm(iterable)|Progress Bar on loops|

* Web


| Library | function / Class etc. | Description |
|-----------|---------------------|----------------|
|Request    |                |                |
|Django    |                     |                |
|Flask    |      |                |
|Falcon||E.g. use for API Mocking/Stubbing|
|BeautifulSoup    |      |
|Selenium  |
|    |      |


* Django Add-ons or Helpful libs when dealing with Django

| Library                           | function / Class etc. | Description                         |
|-----------------------------------|-----------------------|-------------------------------------|
|fernet_fields                      | EncryptedTextField    | Encrypts field in DB                |
|django.contrib.postgres.fields     | JSONField             | JSON Field - deprecated 3.1         |
|django.db.models.JSONField         | JSONField             | JSON Field*                         |
|django.urls.reverse                | reverse()             | Returns relative URI                |
|rest_framework.reverse             | reverse()             | Return absolute URI from WebAPI     |
|uuid                               | models.UUIDField()    | E.g. default=uuid.uuid4             |
|channels.generic.websocket         | AsyncWebsocketConsumer| Websocket implementation            |
|channels.layers                    | get_channel_layer     | Websocket implementation helper     |
|asgiref.sync                       | async_to_sync         | Websocket implementation helper     |
|responses                          | add(), add_callback() | Mock requests library               |
|whitenoise                         | Middleware            | Serves static files for production  |
|nginx                              | Reverse Proxy and an alternative to whitenoise for static   |
|gunicorn                           | WSGI Compatible webserver for django                        |
|djangorestframework                | DRF                                                         |
|drf-yasg (pyyaml, uritemplate)     | Swagger and Redoc API Documentaton for DRF projects         |
|dj-rest-auth                       | Login, Logout, PW Reset, + Registration Endpoint            |
|django-allauth                     | User Registration FLow + Social Auth (combine with dj-rest-auth) |
|django-cors-headers                | CorsMiddleware for CORS HTTP Header                         |
|psycopg2-binary                    | Database Adapter for PostgreSQL                             |

* MariaDB 10.2.7+, MySQL 5.7.8+, Oracle, PostgreSQL, and SQLite 3.9.0+ (with the JSON1 extension enabled).
* ResponseLib - https://github.com/getsentry/responses#basics
* DRF.reverse - https://www.django-rest-framework.org/api-guide/reverse/

* Data Science


| Library | function / Class etc. | Description |
|-----------|---------------------|----------------|
|Numpy    |                     |                |
|Pandas|read_excel, ffill, iloc, iterrows, head, drop, dropna, head, idxmax, isnull, |Working with Dataframes|
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

| Library   | function / Class etc.       | Description                                |
|-----------|-----------------------------|--------------------------------------------|
|Cement     | App, Controller, ex,        | CLI Interface for application              |
|Loguru     |                             |Enhanced logging library                    |
|xy         |                             |                                            |
