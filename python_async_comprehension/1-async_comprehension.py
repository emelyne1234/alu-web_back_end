#!/usr/bin/env python3
"""async comprehensions"""

import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


<<<<<<< HEAD
async def async_comprehension() -> list[float]:
    """returns 10 random numbers"""
    list = [i async for i in async_generator()]
    return list
=======
async def async_comprehension() -> List[float]:
    """ returns 10 random numbers """
    return [y async for y in async_generator()]


if __name__ == "__main__":
    asyncio.run(async_comprehension())
>>>>>>> f75befe12601afd6255bbf8e82f674d1f0aa239d
