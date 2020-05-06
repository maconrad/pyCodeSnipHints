Context Managers and Yield
==========================

## With Statement Demo
* Acquire Lock (Python Threading)
* Filesystem
* aiohttp Session Object (reuse session)

```python
    # Try / Catch 
    try:
        stream = open('demo.txt', 'wt')
        stream.write('abc')
    catch Exception e:
        # Do something
        pass
    finally:
        stream.close()

    # WITH
    with open('demo.txt', 'wt') as stream:
        stream.write('abc')
```

```python
    # Aquire / Lock
    some_lock.acquire()
    try:
        # do something...
    finally:
        some_lock.release()

    # WITH
    with some_lock:
        # do something...
```

***

## Create Context Manager 
* Needs \_\_enter\_\_ and \_\_exit\_\_ Implementations 

```python
    class Connection:
        def __init__(self):
        ...

        def __enter__(self):
        # Initialize connection...

        def __exit__(self, type, value, traceback):
        # Close connection...

    with Connection() as c:
    # __enter__() executes
    ...
    # conn.__exit__() executes
```
***

## Create Context Manager with Yield 
* contextmanager manager decorator
  1. Before yield is executed when entering the with block (1st print)
  2. Then the block is executed (print in with block)
  3. Finally rest of the tag function is executed (2nd print).

```python
    from contextlib import contextmanager

    @contextmanager
    def tag(name):
        print(f"<{name}>")
        yield
        print(f"</{name}>")

    with tag("h1"):
        print("This is Title.")
```

## Links
* See Threading [Python Docs](https://docs.python.org/3/library/threading.html#with-locks)
* See Filesystem [Real Python](https://realpython.com/working-with-files-in-python/)
* See Martin Heinz [Blog](https://martinheinz.dev/blog/1)