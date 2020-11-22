Classes and Mixins
==================

## Classes - Basics
* Classes are reusable and group data and operations together
* Class = Noun (PascalCasing)
* Property of Class = Adjective
* Methods = Verbs
* self => think this (access to current instance/object)

```python
    class Actor():
        def __init__(self, name):
            # Constructor
            self.name = name # Field

        def say_hello(self):
            print('Hello, ' + self.name)
```

```python
    # Using Class
    actor1 = Actor('Batman')
    actor1.name = 'Robin'
    actor1.say_hello()
```

## Classes - Accessibility & Properties
* Everything is Public
* No Public / Protected / Private keyword in Python (think C# / Java)
* Convention for suggestions
  * _ = should be avoided
  * __ = do not use (internal)
* Property = field style access, but method behind the scenes
  * Property getter uses @property, setter uses @propertyname

```python
    class Actor():
        def __init__(self, name):
            # Access __name via property (behind scenes)
            # Always use property -> validation
            self.name = name # Property

        @property
        def name(self):
            return self.__name # Field

        @name.setter
        def name(self, value)
            # Optional validation
            self.__name = name
```

## Inheritance
* Generalization <> Spezialition Relationship
  * "is a" Relationship
    * Student is a Person
    * SqlConnection is a DatabaseConnection
  * Everything inherits from Object
    * Override \_\_methods\_\_ (like \_\_str\_\_)
  * All methods in python are "virtual"=can be overriden
  * super keyword to access parent class
    * Must always call parent constructor!
* Composition (done with Properties)
  * "has a" Relationship
  * Student has a StudentId
  * DatabaseConnection has a ConnectionString

```python
    class Person():
        def __init__(self, name):
            self.name = name # Field

        def say_hello(self):
            print('Hello, ' + self.name)

        # Override
        def __str__(self):
            return self.name

    class Actor(Person):
        def __init__(self, name, movie):
            # super in init Must always be called
            super().__init__(name)
            self.movie = movie

        def act(self):
            print("Play in: " + self.movie)

        # Override
        def say_hello(self):
            # Parent call, not auto calls parent
            super().say_hello()
            print('xy')

```
```python
    # Using Class
    actor1 = Actor('Batman', 'Robin Sucks')
    actor1.say_hello()
    actor1.act()
    print(isinstance(actor1, Actor))    # True
    # F-String because auto-string conversion (here boolean)
    print(f'Is it an Actor? {isinstance(actor1, Actor))}'    # True
    print(isinstance(actor1, Person))   # True
    print(issubclass(Actor, Person))    # True
```

## Mixins (Multiple Inheritance)
* C# / Java not supported (because can get messy)
* Used mostly when clipping into a framework (+ e.g. own class hiearchy)
* Own Creation not usual
* Example: Django

```python
    # Using Class
    Class Loggable:
        def __init__(self):
            self.title = ''
        def log(self):
            print('Log Msg from ' + self.title)

    Class Connection:
        def __init__(self):
            self.server = ''
        def connect(self):
            print('Connecting to DB ' + self.server)

    Class SqlDatabase(Connection, Loggable):
        def __init__(self):
            self.title = 'SQL Connection Demo'
            self.server = 'Some_Server'

    def framework(item):
        if isinstance(item, Connection):
            item.connect()
        if isinstance(item, Loggable):
            item.log()

    sql_connection = SqlDatabase()
    framework(sql_connection)
```

## Inhertitance with Meta
* TODO

## Real World Example
* Django RestFramework makes use of Mixins

```python
    from snippets.models import Snippet
    from snippets.serializers import SnippetSerializer
    from rest_framework import mixins
    from rest_framework import generics

    class SnippetList(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
        queryset = Snippet.objects.all()
        serializer_class = SnippetSerializer

        def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)

        def post(self, request, *args, **kwargs):
            return self.create(request, *args, **kwargs)
```

## Links
* Django Restframework [DRF Mixins](https://www.django-rest-framework.org/tutorial/3-class-based-views/)
* Tutorial Mixins [MS Tutorial](https://www.youtube.com/watch?v=JgT3jIh05po&list=PLlrxD0HtieHiXd-nEby-TMCoUNwhbLUnj&index=12)
