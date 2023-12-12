#!/usr/bin/env python3
"""import async_generator from the previous task and then write a coroutine callled async_comprehension the takes no arguments.
the coroutine will collect ten random numbers using an async comprehension over
async_genarator, the return the ten ramdom numbers.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """Return the ten random numbers  """
    results = [i async for i in async_generator()]
    return results
    
