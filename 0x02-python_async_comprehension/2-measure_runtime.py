#!/usr/bin/env python3

''' Desription: Import async_comprehension from the previous file and write a
                measure_runtime coroutine that will execute async_comprehension
                four times in parallel using asyncio.gather.
                measure_runtime should measure the total runtime and return it.
                Notice that the total runtime is roughly 10 seconds, explain
                it to yourself.
'''

import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Collect 10 random numbers using an async comprehensing,
    then return the 10 random numbers.
    """
    start: float = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end: float = time.perf_counter()
    return (end - start)
