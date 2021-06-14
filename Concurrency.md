Async & Await
==========================

## Slow Operations
* Web Calls (e.g. REST)
* Network IO
* Complex Data Processing
* Solvable with
  * Async / Await
  * Concurrency (Threading)
  * Parallelism

## Asyncio Module
* Async / Await
* streams
* synchronization locks
* Exception mgmt
* Tasks that runs async
  * When done, inform -> Callback
* Async keyword
  * Flag as async function = can be awaited
  * Tells runtime, there will be an wait command in block
  * With needs to be marked as well
* await keyword (similar to join in Threading)
  * logically pause code until Taks finished
  * (Think Promise from JS)
  * Needs to be inside async construct/block
* aiohttp
* Introduced in 3.4, changed often until 3.7


```python
import aiohttp
import asyncio
from timeit import default_timer

async def load_data(session, delay):
  async with session.get(f'https://httpbin.org/delay/{delay}') as resp:
    await resp.text()

async def main():
  start_time = default_timer()

  async with aiohttp.ClientSession() as session:
    two_sec_delay_task = asyncio.create_task(load_data(session, 2))
    three_sec_delay_task = asyncio.create_task(load_data(session, 3))

    await asyncio.sleep(1)
    print('do other stuff')

    two_result = await two_sec_delay_task
    three_result = await three_sec_delay_task

    elapsed_time = default_timer() - start_time
    print(f'The operation took {elapsed_time:.2} seconds')

# Cannot just be called with main() as it is async
# x = await main()

# Better use asyncio
asyncio.run(main())
```

## Links
* See [RealPython AsyncIO](https://realpython.com/async-io-python/)
* See [RealPython Threading](https://realpython.com/intro-to-python-threading/)
* See [RealPython Concurrency](https://realpython.com/python-concurrency/)
* See [Microsoft](https://www.youtube.com/watch?v=aHubP4jcvOk&list=PLlrxD0HtieHiXd-nEby-TMCoUNwhbLUnj&index=18)
