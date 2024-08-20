# Python - Async
asyncronous code is a style of programming implemented across a wide range of programming languages, it let's code run concurrently or at least gives you the feel of concurrency, as we will see.


> `quick definition`: asyncio is a library to write concurrent code using the async/await syntax. asyncio uses cooperative multi-tasking rather than multi-threading, so it is not parallelism neither is it multi-threaded. Infact it is single threaded.

> `async/await` are python keywords that let's us define coroutines.

> `coroutines` is a function that is awaitable, it can pause and cede (give up) control to event loop, so that other task that a ready to execute can then run.
