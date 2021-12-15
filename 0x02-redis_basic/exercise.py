#!/usr/bin/env python3
"""
Writing strings to redis
"""
from typing import Union, Callable
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

    def get(self, key: str, fn: Callable = None):
        """get key from redis database"""
        if fn is not None:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """convert binary to string"""
        return self._redis.get(key).decode("utf-8")

    def get_int(self, key: str) -> int:
        """convert binary to string then to int"""
        return int(self._redis.get(key).decode("utf-8"))
