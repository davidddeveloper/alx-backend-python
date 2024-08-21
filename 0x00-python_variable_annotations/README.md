# Python - Variable Annotations

> `annotation` - a text that describes/explains image or other text

In the context of python, Variable Annotation is a way of telling whoever is reading our code, what type(int, str, bool etc) a variable supposed to hold or the type a function receive as argument or the type it returns.

`dynamically typed` - In contrast to statically typed languages like C, Python is dynamically typed and what that means is - the type is determined at run time upon assignment of a value and a variable that hold say float can be change elsewhere to int. - `documentation`

`Note` - python does not enforce it annotation. However, python annotation can be enforced by third party tools/code like linters or code editors. - `validation`

## examples
`variables`
> first_name: str = 'David'

`function`

    def get_name(name: str) -> str:
        print(name)

a

    from typing import Union
    def get_name_or_age(name_or_age: Union[str, int]) -> Union[str, int]:
        print(name_or_age)

``

    `#` newer version of python
    def get_name_or_age(name_or_age: str | int) -> str | int:
        print(name_or_age)


` callbacks`

    from typing import Callable
    def call_func(x: int) -> Callable[[int, float], List[float]]:
        some_func(x: int, y: float) -> List[float]:
          return [x * y]

` Generators `

    from typing import Generator, Iterable, Iterator
    # Generator[yieldType, sendType, returnType]
    def generate() -> -> Generator[int]
        for i in range(1, 6):
            yield i
    
    # iterable or Iterator
    def generate() -> Iterator[int]
        for i in range(1, 6):
            yield i

` Async generator `

    from typing import AsyncGenerator
    async def echo_round() -> AsyncGenerator[int, float]:
    sent = yield 0
    while sent >= 0.0:
        rounded = await round(sent)
        sent = yield rounded