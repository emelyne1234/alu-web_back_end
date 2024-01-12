#!/usr/bin/env python3
"""async comprehensions"""

import asyncio
import uniform
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    """ returns 10 random numbers """
    return [y async for y in async_generator()]
