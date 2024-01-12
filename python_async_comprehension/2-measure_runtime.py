#!/usr/bin/env python3
""" runtime for four parallel comprehensions """
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ returns the measured total runtime """
    p = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    elapsed = time.perf_counter() - p
    return elapsed
