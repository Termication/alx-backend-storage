#!/usr/bin/env python3
"""
Module for working with Redis, providing basic caching functionality, 
method call tracking, and call history.
"""
import uuid
import redis
from functools import wraps
from typing import Any, Callable, Union


def count_calls(method: Callable) -> Callable:
    '''Decorator to count the number of times a method is called.

    This decorator increments a counter in Redis each time the decorated
    method is invoked.

    Args:
        method (Callable): The method whose calls are being tracked.

    Returns:
        Callable: The wrapped method with call count tracking.
    '''
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        '''Increments the method call count in Redis and invokes the method.
        '''
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return invoker


def call_history(method: Callable) -> Callable:
    '''Decorator to track the history of inputs and outputs of a method.

    This decorator stores the arguments and return value of each call to the
    method in Redis, allowing a call history to be recorded.

    Args:
        method (Callable): The method to track input/output history for.

    Returns:
        Callable: The wrapped method with input/output tracking.
    '''
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        '''Records method inputs and outputs in Redis, then calls the method.
        '''
        in_key = '{}:inputs'.format(method.__qualname__)
        out_key = '{}:outputs'.format(method.__qualname__)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(in_key, str(args))
        output = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(out_key, output)
        return output
    return invoker


def replay(fn: Callable) -> None:
    '''Displays the history of calls to a method, including inputs and outputs.

    This function retrieves the method's call history (number of calls, 
    arguments, and return values) from Redis and prints it in a readable format.

    Args:
        fn (Callable): The method whose call history is being displayed.
    '''
    if fn is None or not hasattr(fn, '__self__'):
        return
    redis_store = getattr(fn.__self__, '_redis', None)
    if not isinstance(redis_store, redis.Redis):
        return
    fxn_name = fn.__qualname__
    in_key = '{}:inputs'.format(fxn_name)
    out_key = '{}:outputs'.format(fxn_name)
    fxn_call_count = 0
    if redis_store.exists(fxn_name) != 0:
        fxn_call_count = int(redis_store.get(fxn_name))
    print('{} was called {} times:'.format(fxn_name, fxn_call_count))
    fxn_inputs = redis_store.lrange(in_key, 0, -1)
    fxn_outputs = redis_store.lrange(out_key, 0, -1)
    for fxn_input, fxn_output in zip(fxn_inputs, fxn_outputs):
        print('{}(*{}) -> {}'.format(
            fxn_name,
            fxn_input.decode("utf-8"),
            fxn_output,
        ))


class Cache:
    '''Represents a caching system using Redis as the backend.

    This class allows data to be stored, retrieved, and managed in a Redis
    instance. It also provides functionality to track method call histories
    and call counts.
    '''
    def __init__(self) -> None:
        '''Initializes the Cache class and flushes the Redis database.
        '''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Stores a value in Redis and returns its unique key.

        Args:
            data (Union[str, bytes, int, float]): The data to store.

        Returns:
            str: The key associated with the stored data.
        '''
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key

    def get(
            self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        '''Retrieves a value from Redis by its key, optionally applying a 
        transformation function to the value.

        Args:
            key (str): The key of the value to retrieve.
            fn (Callable, optional): A function to apply to the retrieved value. Defaults to None.

        Returns:
            Union[str, bytes, int, float]: The retrieved value, possibly transformed.
        '''
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        '''Retrieves a string value from Redis.

        Args:
            key (str): The key of the value to retrieve.

        Returns:
            str: The value as a string.
        '''
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        '''Retrieves an integer value from Redis.

        Args:
            key (str): The key of the value to retrieve.

        Returns:
            int: The value as an integer.
        '''
        return self.get(key, lambda x: int(x))
