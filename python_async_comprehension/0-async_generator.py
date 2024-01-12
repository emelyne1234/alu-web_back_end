#!/usr/bin/env python3
"""async generator"""
from typing import Generator
import random
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """generates a random nbr btn 0-10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
