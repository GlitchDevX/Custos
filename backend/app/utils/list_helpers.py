from typing import Iterable
from typing import Callable

def map_as_list(func: Callable, iter: Iterable):
    return list(map(func, iter))

def filter_as_list(func: Callable, iter: Iterable):
    return list(filter(func, iter))