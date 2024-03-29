"""Provides a simple function sum(values) that includes rigorous error checking."""

import collections

def sum(values):
    if not isinstance(values, collections.abc.Iterable):
        raise TypeError('parameter must be an iterable type')
    total = 0
    for v in values:
        if not isinstance(v, (int, float)):
            raise TypeError('elements must be numeric')
        total = total+ v
    return total
