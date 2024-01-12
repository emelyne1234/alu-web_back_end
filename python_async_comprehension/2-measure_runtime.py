#!/usr/bin/env python3
""" runtime for four parallel comprehensions """
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ returns the measured total runtime """
    start_time = time()
    tasks = [async_comprehension() for i in range(4)]
    await gather(*tasks)
    end_time = time()
    return (end_time - start_time)
