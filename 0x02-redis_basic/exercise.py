#!/usr/bin/env python3
"""
writing strings to redis
"""
import redis
from uuid import uuid4
from typing import Union


class Cache:
    def __init__(self):
        """ stores an instance of reddis cient
            as a private variable name _redis
            and flush the instance using flush
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[int, float, bytes, str]) -> str:
        """ create a unique key and stores the data"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
