#!/usr/bin/env python3
"""async comprehensions"""

import asyncio
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def async_comprehension() -> list[float]:
    """ returns 10 random numbers """
    return [y async for y in async_generator()]
