What's new
===============

## 3.4
* asyncio Module (See Concurrency.md)
  * Shoud use 3.7 with asyncio

```python
    import asyncio

    async def count():
        print("One")
        await asyncio.sleep(1)
        print("Two")

    async def main():
        await asyncio.gather(count(), count(), count())

    if __name__ == "__main__":
        import time
        s = time.perf_counter()
        asyncio.run(main())
        elapsed = time.perf_counter() - s
        print(f"{__file__} executed in {elapsed:0.2f} seconds.")

        # Output: One One One Two Two Two
        # Sync: One Two One Two One Two
```
***
## 3.5
* Type Hints - PEP 484

## 3.6
* Pathlib
    * Better perfromance than os.path
    * Class based

```python
    from pathlib import Path

    # Working dir
    cwd = Path.cwd()
    parent = cwd.parent
    print(cwd)
    print(parent.is_dir())
    print(parent.is_file())

    # List child dirs
    for child in parent.iterdir():
        if child.is_dir()
            print(child)

    # Full Path creation
    new_file_path = Path.joinpath(cwd, 'new_file.txt')

    # File info
    print(new_file)
    print(new_file_path.name)
    print(new_file_path.suffix)
    print(new_file_path.parent.name)
    print(new_file_path.stat().st_size)

    # Validate if already exists before creating
    print(new_file_path.exists())

    # Read and write
    stream = open('demo.txt') # Default read
    stream2 = open('demo2.txt', 'wt') # Write Text
    names = ['wulu', 'hugu']
    print(stream.readable())
    print(stream.writable())
    print(stream.read(1)) # Read 1st char
    print(stream.readline()) # Reads now from 2ncd char until end (Pointer)
    stream2.write('H')
    stream2.writelines(['He', 'Ha']) # No new lines
    stream2.writelines('\n'.join(names))
    stream2.seek(0) #Put cursor back to start
    stream2.write('overriding')
    stream2.write('\n')
    stream.close()
    stream2.flush() # Write to file
    stream2.close() # Flush and close stream

```

* F-Strings - PEP498
```python
    # Before
    print('He said his name is {name}.'.format(name=name))
    print('He said his name is {}.'.format(name))

    # Now
    print(f'He said his name is {name}.')
```



* Enhancing of Type Hints (PEP 484)
  * Now also for Variables (PEP 526)

```python
    class A:
        name:str

    A.__annotations__
    # Output: {'name': <class 'str'>}
```

* UTF-8 on Windows (PEP 528, 529)
* Others:
  * Async Generators & Comprehension (PEP 525, PEP 530)
  * Meta obsolete (PEP 487)
  * Secrets Module for strong passwords
  * Dict uses less memory
  * Interpreter abbreviates long sequences of tracebacks
  * json module supports binary

***

## 3.7
* breakpoint()
  * PYTHONBREAKPOINT=0 ignores calls to breakpoint()
*

```python
    # Before
    def divide(e, f):
        import pdb; pdb.set_trace()
        return f / e

    # Now
    def divide(e, f):
        breakpoint()
        return f / e

```

## 3.8
* Walrus Operator (:=) - PEP572
  * assign variables inside an expression
* Others
  * Positional only arguments - PEP570
  * Easier debugging of f-strings
* Final Keywork - PEP591
  * On Class = No Inheritance
  * On Var = No reassigning
  * On Method = No Override
* Example:

```python
    # BEFORE
    Item = getItem()
    while Item:
        do_something(item)
        Item = getItem()

    # Now
    while Item:= getItem():
        do_something(Item)
```


## 3.9
* Dict Merge Operator

## 3.10
* Annotations now default (PEP563)
  * Not anymore via future
* Also TypeAlias, TypeUnion annotations (PEP613, PEP604)

  ```python
      # BEFORE
      from __future__ import annotations
      from typing import Union, Any, Type, SupportsFloat

      ...
      def __init__(self, x: SupportsFloat, y: SupportsFloat): -> float
        ...
      # Now
      ...
  ```

## Links
* See DataFlair [Py36](https://data-flair.training/blogs/whats-new-in-python-3-6/)
* See RealPython [Py37](https://realpython.com/python37-new-features/)
* See DataFlair [Py38](https://data-flair.training/blogs/whats-new-in-python/)
