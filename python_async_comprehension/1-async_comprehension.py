#!/usr/bin/env python3
"""async comprehensions"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    """returns 10 random numbers"""
    list = [i async for i in async_generator]
    
