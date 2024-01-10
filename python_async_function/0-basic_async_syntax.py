#!/usr/bin/env python3
"""async syntax basics"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """returns a random delay btn 0 and max_delay secs eventuallly"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
