#!/usr/bin/env python3
'''Module for caching HTTP request data and tracking the number of requests.
'''
import redis
import requests
from functools import wraps
from typing import Callable


redis_store = redis.Redis()
'''A Redis instance for caching and tracking request data.
'''


def data_cacher(method: Callable) -> Callable:
    '''Decorator to cache the result of a method that fetches data.

    This decorator caches the result of fetching data from a URL and tracks
    how many times the URL is requested.
    
    Args:
        method (Callable): The function that fetches data to be cached.

    Returns:
        Callable: The wrapped function with caching and tracking.
    '''
    @wraps(method)
    def invoker(url: str) -> str:
        '''Increments request count and caches the result for a specific URL.

        If the result for the URL is already cached, returns the cached result.
        Otherwise, fetches the result, caches it for a set time, and resets
        the request count.

        Args:
            url (str): The URL whose content is being fetched.

        Returns:
            str: The content of the fetched URL, either from the cache or a new request.
        '''
        redis_store.incr(f'count:{url}')
        cached_result = redis_store.get(f'result:{url}')
        if cached_result:
            return cached_result.decode('utf-8')
        result = method(url)
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:{url}', 10, result)  # Cache the result for 10 seconds
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    '''Fetches and caches the content of a URL, tracking the number of requests.

    The function uses the `data_cacher` decorator to cache the URL's content
    and track how many times the URL has been accessed.

    Args:
        url (str): The URL whose content is being fetched.

    Returns:
        str: The content of the fetched URL.
    '''
    return requests.get(url).text
