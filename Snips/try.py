# nums = [1, 2, 3, 4]

# for num in nums:
#     print(num)

from typing import SupportsFloat, TypeVar, Generic, Sequence, List

Vector = List[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

new_vector = scale(2.0, [1.0, -4.2, 5.4])

# Typing 2 - TypeVar, Generics



T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        # Create an empty list with items of type T
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def empty(self) -> bool:
        return not self.items

# Construct an empty Stack[int] instance
stack = Stack[int]()
stack.push(2)
stack.pop()
# stack.push('x')        # Type error
stack.push(5)        # Type error
stack.pop()
# stack.pop()


# T = TypeVar('T')  # Can be anything
S = TypeVar('S')

# Must be str or bytes -> Value restriction
AnyStr = TypeVar('AnyStr', str, bytes)


def repeat(x: T, n: int) -> Sequence[T]:
    return [x]*n


def concat(a: AnyStr, b:AnyStr) -> AnyStr:
    return a + b

print(concat('Helo', 'World'))
# Uncomment and run python -m mypy Snips/try.py   
# reveal_type(concat(b'foo', b'bar'))
print(concat(10, 10)) # Works but type checker complains!

print(repeat(x=10, n=10))
# c = T(10)
# d = AnyStr(10.2)
# print(d)


# Typing 7 - Generic
from typing import TypeVar, Generic
import logging
from logging import Logger

# TypeVar can be of any type = unbounded = no restrictions
# Otherwise TypeVar would need to be defined like TypeVar('T', float, int) for example
T = TypeVar('T')

# By inheriting from Generic own classes can be made generic
class LoggedVar(Generic[T]):
    def __init__(self, value: T, name: str) -> None:
        self.name = name
        self.value = value

    def set(self, new: T) -> None:
        self.log('Set ' + repr(self.value))
        self.value = new

    def get(self) -> T:
        self.log('Get ' + repr(self.value))
        return self.value

    def log(self, message: str) -> None:
        print('{}: {}'.format(self.name, message))


int_logger = LoggedVar[int](value=5, name='Integer Logger')
int_logger.set(new=10)
int_logger.set(new=7)
int_logger.set(new='halo')
int_logger.set(new=8)

str_logger = LoggedVar[str](value=5, name='Integer Logger')
str_logger.set(new=10)
str_logger.set(new=7)
str_logger.set(new='halo')
str_logger.set(new=8)


from typing import Generic, overload, Sequence, TypeVar, Union

ValueType = TypeVar('ValueType')

class Series(Generic[ValueType]):
    def __init__(self, data: Sequence[ValueType]):
        self._data = data

    @overload
    def __getitem__(self, index: int) -> ValueType:
        ...
    
    @overload
    def __getitem__(self, index: slice) -> Sequence[ValueType]:
        ...

    def __getitem__(self, index: Union[int, slice]) -> Union[ValueType, Sequence[ValueType]]:
        return self._data[index]

s = Series[int]([2, 4, 6, -1, 3])
s[0] + 5
sum(s[1:4])
