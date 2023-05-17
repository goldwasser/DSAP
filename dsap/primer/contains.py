"""Provides a simple function contains(data,target)."""

def contains(data, target):
    """Return True if target is found in data, False otherwise."""
    for item in data:
        if item == target:               # found a match
            return True
    return False
