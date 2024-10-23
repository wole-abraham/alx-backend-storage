#!/usr/bin/env python3
"""
writing strings to redis
caching is the first step
"""
import redis
from uuid import uuid4
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> callable:
    """returns a callable"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper for the decorated function """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> callable:
    """store the history of inputs and outputs"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper for the decorated function"""
        input = str(args)
        self._redis.rpush(key + ":inputs", input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(key + ":outputs", output)
        return output
    return wrapper


def replay(fn: Callable):
    """display the history of calls of a particular function"""
    r = redis.Redis()
    function_name = fn.__qualname__
    value = r.get(function_name)
    try:
        value = int(value.decode("utf-8"))
    except Exception:
        value = 0

    # print(f"{function_name} was called {value} times")
    print("{} was called {} times:".format(function_name, value))
    # inputs = r.lrange(f"{function_name}:inputs", 0, -1)
    inputs = r.lrange("{}:inputs".format(function_name), 0, -1)

    # outputs = r.lrange(f"{function_name}:outputs", 0, -1)
    outputs = r.lrange("{}:outputs".format(function_name), 0, -1)

    for input, output in zip(inputs, outputs):
        try:
            input = input.decode("utf-8")
        except Exception:
            input = ""

        try:
            output = output.decode("utf-8")
        except Exception:
            output = ""

        # print(f"{function_name}(*{input}) -> {output}")
        print("{}(*{}) -> {}".format(function_name, input, output))


class Cache:
    """Create a Cache class"""

    def __init__(self):
        """ stores an instance of reddis cient
            as a private variable name _redis
            and flush the instance using flush
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[int, float, bytes, str]) -> str:
        """ create a unique key and stores the data"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[callable] = None):
        """ get value from the key """
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        return data

    def get_str(self, data: str) -> str:
        """ automatically parametrize Cache.get with the correct
        conversion function"""
        data = self._redis.get(data)
        return data.decode("utf-8")

    def get_int(self, data: str) -> int:
        """automatically parametrize Cache.get with the correct
        conversion function"""
        data = self._redis.get(data)
        try:
            data = int(data.decode("utf-8"))
        except Exception:
            value = 0
        return value
