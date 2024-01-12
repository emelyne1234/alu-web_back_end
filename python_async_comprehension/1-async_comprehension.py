#!/usr/bin/env python3
"""async comprehensions"""

import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ returns 10 random numbers """
    return [y async for y in async_generator()]


if __name__ == "__main__":
    asyncio.run(async_comprehension())