"""Provides a simple function count(data,target)."""

def count(data, target):
    """Return the number of occurrences of target within sequence data."""
    n = 0
    for item in data:
        if item == target:               # found a match
            n += 1
    return n
