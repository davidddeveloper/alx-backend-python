# Python - Async Comprehension

`Read this first` [async in python](/alx-backend-python/0x01-python_async_function/README.md)

Remember `list comprehension` `dict comprehension` or set `comprehension`<br><br>
`l = [i for i in range(1, 5) if i % 2]`<br>
`j = {i for i in range(1, 5) if i % 2}`<br>
`k = {a:b for a,b in enumerate([2, 4, 6, 8])}`<br>

Well async comprehension are just like that the only thing is that the keyword `async`/`wait` should be use.

Note also that an async comprehension should only be used inside of a async function ie a coroutine.

## examples 
assuming we are inside of a coroutine

`async for`

    result = [await fun() for fun in funcs]
    result = {await fun() for fun in funcs}
    result = {await fun() async for fun in funcs}

    oddnumbers = [i async for i in numbers(10) if i % 2]

`note that` - funcs and numbers(10) should be a coroutine or async function. This is one of the downsides of async comprehension.

`async generators`
first let us learn about generators in python

`generators`<br>
generators are special type of iterable like list or set, allowing you to iterate over a sequence of values lazily, meaning they generate a value on the fly and only when it is required. Generators are efficient for working with large dataset or infinite sequence, this is because the data will not be loaded in memory all at once.<br>

They are constructed like normal functions and the `yield` keyword.<br>
The `yeild` keyword is powerful, it will pause the iterable and resume from where it left off. Awesome right!

example:<br>

    def generate():<br>
        for i in range(1, 6):
            yield i
    
    > type(generate())`
    > <class 'generator'>

calling generate will return a generator instance that you can iterate over to print it values, like so:

    generator_instance = generate()
    for i in generator_instance:
        print(i)

`not that` after the loop generator_instance can no longer be used, this is because once you finishing iterating over a generator instance it can't be re-used. However, to get the values again you can call generate() again.

`generator comprehension`

    gencompre = (i for i in range(1, 6))

note that gencompre is not callable neither is it subscriptable. It is a generator instance, so to get it values you just loop through it directly like we did above. The benefit of using the function generate  over the generator comprehesion is that, whenever you need a new object you just call generate.


`async generator now`<br>
example:

    async_gencompre = (i ** 2 async for i in agen())