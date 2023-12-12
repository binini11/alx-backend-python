#!/usr/bin /env python3
""" write a coroutin called async_generator thet takes no arguments.
 The coroutine will loop 1- times, each time asynchronously wait 1 second,
 then yeild a random number b/n 0 and 1. Use the random module
 """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
     """ Loop 10 times, wait 1 second """

     for i in range(10):
         await asyncio.sleep(1)
         yield random.random() * 10
