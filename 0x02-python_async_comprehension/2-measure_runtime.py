#!/usr/bin/env python3
"""import async_comprehension from the previous task ahd write a measure_runtime
 coroutine that will execute async_comprehension fout times inparallel using asyncio.gather.

 measure_runtime shouy measure the total runtime and return it.
 notice the total runtime is roughly ten seconds, explain it to yourself
 """

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
     """ measure the totall runtime  """
     start_time = time.time()
     await asyncio.gather(*(async_comprehension() for i in range(4)))
     end_time = time.time()
     return end_time - start_time
