#!/usr/bin/env python3
"""
Writing strings to redis
"""
from typing import Union
import redis
import uuid


class Cache:
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = uuid.uuid1()
        self._redis.set(str(key), data)
        return str(key)
